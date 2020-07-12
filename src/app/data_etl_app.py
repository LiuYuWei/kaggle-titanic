"""This file is the pipeline for data etl"""

# import relation package.

# import project package.
from config.config_setting import ConfigSetting
from src.service.data_etl_service import DataEtlService

class DataEtlApp:
    def __init__(self):
        config_setting = ConfigSetting()
        self.config = config_setting.yaml_parser()
        self.log = config_setting.set_logger(["data_etl_app"])
        self.data_etl_service = DataEtlService()
    
    def start(self):
        self.extract()
        self.transform()
        self.load_to()
        self.finish()

    def extract(self):
        self.data_etl_service.load_data()
        self.log.info('=== Finish extract the data. ===')

    def transform(self):
        self.data_etl_service.title_generator()
        self.data_etl_service.sex_generator()
        self.data_etl_service.age_generator()
        self.data_etl_service.embark_generator()
        self.data_etl_service.cabin_generator()
        self.data_etl_service.fare_generator()
        self.data_etl_service.remove_feature()
        # numerical_features, categorical_features = self.data_etl_service.feature_selection()
        self.data_etl_service.fill_na_value()
        self.log.info('=== Finish transform the data. ===')

    def load_to(self):
        self.data_etl_service.save_dataframe()
        self.data_etl_service.save_label()
        self.log.info('=== Finish load the data to file. ===')

    def finish(self):
        pass
