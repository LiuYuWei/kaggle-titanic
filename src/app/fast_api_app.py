"""This file is the pipeline for api"""

# import relation package.
import pandas as pd

# import project package.
from config.config_setting import ConfigSetting
from src.service.train_eval_service import TrainEvalService

class FastApiApp:
    def __init__(self):
        config_setting = ConfigSetting()
        self.config = config_setting.yaml_parser()
        self.log = config_setting.set_logger(["data_etl_app"])
        self.train_eval_service = TrainEvalService()
    
    def prediction(self, data):
        data = pd.DataFrame.from_dict(data)
        result = self.train_eval_service.prediction(predict_data = data)
        return result
    
    
