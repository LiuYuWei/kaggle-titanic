"""This file is the pipeline for data etl"""

# import relation package.
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB


# import project package.
from config.config_setting import ConfigSetting


class TrainEvalService:
    def __init__(self):
        config_setting = ConfigSetting()
        self.config = config_setting.yaml_parser()
        self.log = config_setting.set_logger(["training_service"])
        self.df = {}
        self.label = []
        self.data = {}
        self.model = None

    def read_preprocess_data(self, save_file_path=None):
        if save_file_path is None:
            save_file_path = self.config['load_to']['save_file_path']
        self.df['train'] = pd.read_csv("{}/{}".format(save_file_path, 'train.csv'))
        self.df['test'] = pd.read_csv("{}/{}".format(save_file_path, 'test.csv'))
        self.log.info('Successfully read training and testing data.')

    def read_preprocess_label(self, save_file_path=None):
        if save_file_path is None:
            save_file_path = self.config['load_to']['save_file_path']
        with open("{}/{}".format(save_file_path, 'training_label.pkl'), 'rb') as file:
            self.label = pickle.load(file)
        self.log.info('Successfully read label file data.')

    def train_test_split(self):
        self.data['x_train'], self.data['x_valid'], self.data['y_train'], self.data['y_valid'] = train_test_split(
            self.df['train'], self.label, test_size=0.05, random_state=42)
        self.log.info('Successfully split the training data and validation data.')
        self.log.info('shape of training data: {}'.format(len(self.data['x_train'])))
        self.log.info('shape of validation data: {}'.format(len(self.data['x_valid'])))
    
    def svm_training(self):
        self.model = SVC()
    
    def knn_training(self):
        self.model = KNeighborsClassifier(n_neighbors = self.config['knn']['n_neighbors'])
    
    def decision_tree_training(self):
        self.model = DecisionTreeClassifier()
    
    def rf_training(self):
        self.model = RandomForestClassifier(n_estimators = self.config['rf']['n_estimators'])
    
    def gnb_training(self):
        self.model = GaussianNB()
    
    def gradient_boosting_training(self):
        self.model = GradientBoostingClassifier(n_estimators=10, learning_rate=1,max_features=3, max_depth =3, random_state = 10)
    
    def ada_boost_training(self):
        self.model = AdaBoostClassifier()

    def model_fit(self):
        self.model.fit(self.data['x_train'], self.data['y_train'])
    
    def prediction(self, save_file_path = None, predict_data = None):
        if predict_data is None:
            predict_data = self.data['x_valid']
        if self.model is None:
            if save_file_path is None:
                save_file_path = self.config['load_to']['save_file_path']
            with open("{}/model/{}".format(save_file_path, self.config['predict']['model_path']), 'rb') as file:
                self.model = pickle.load(file)
        validation_prediction = list(self.model.predict(predict_data))
        self.log.info("Prediction: {}".format(validation_prediction))
        return validation_prediction

    def evaluate(self, validation_prediction = None):
        if validation_prediction is None:
            validation_prediction = self.prediction()
        self.log.info("Evaluation report:\n{}".format(classification_report(self.data['y_valid'], validation_prediction)))
    
    def model_save(self, model, save_file_path=None):
        if save_file_path is None:
            save_file_path = self.config['load_to']['save_file_path']
        file = open("{}/model/training_model_{}.pkl".format(save_file_path, model), 'wb')
        pickle.dump(self.model, file)
        file.close()