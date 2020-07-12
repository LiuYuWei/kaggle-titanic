"""This file is the pipeline for data etl"""

# import relation package.

# import project package.
from config.config_setting import ConfigSetting
from src.service.train_eval_service import TrainEvalService

class TrainEvalApp:
    def __init__(self):
        config_setting = ConfigSetting()
        self.config = config_setting.yaml_parser()
        self.log = config_setting.set_logger(["data_etl_app"])
        self.train_eval_service = TrainEvalService()
    
    def start(self, model='lr'):
        self.read_data()
        self.train_test_split()
        self.training_model(model)
        self.evaluate()

    def read_data(self):
        self.train_eval_service.read_preprocess_data()
        self.train_eval_service.read_preprocess_label()
    
    def train_test_split(self):
        self.train_eval_service.train_test_split()
    
    def training_model(self, model):
        if model == 'svm':
            self.train_eval_service.svm_training()
        elif model == 'knn':
            self.train_eval_service.knn_training()
        elif model == 'tree':
            self.train_eval_service.decision_tree_training()
        elif model == 'rf':
            self.train_eval_service.rf_training()
        elif model == 'gnb':
            self.train_eval_service.gnb_training()
        elif model == 'gb':
            self.train_eval_service.gradient_boosting_training()
        elif model == 'ada':
            self.train_eval_service.ada_boost_training()

        if self.train_eval_service.model is not None:
            self.train_eval_service.model_fit()

    def evaluate(self):
        if self.train_eval_service.model is not None:
            validation_prediction = self.train_eval_service.prediction()
            self.train_eval_service.evaluate(validation_prediction)

    def finish(self):
        pass
