"""This file is the pipeline for api"""

# import relation package.

# import project package.
from config.config_setting import ConfigSetting

class FastapiService:
    def __init__(self):
        config_setting = ConfigSetting()
        self.config = config_setting.yaml_parser()
        self.log = config_setting.set_logger(["data_etl_app"])
        self.fast_api_service = FastApiService()
    
    
