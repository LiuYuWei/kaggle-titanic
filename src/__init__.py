"""This file creates the flask service."""
# coding=utf-8
# import relation package.
from fastapi import FastAPI
from pydantic import BaseModel

# import project package.
from config.config_setting import ConfigSetting
from src.app.fast_api_app import FastApiApp

def create_app():
    """Create flask app service."""
    config_setting = ConfigSetting()
    log = config_setting.set_logger("[flask_app]")
    config = config_setting.yaml_parser()
    fast_api_app = FastApiApp()
    app = FastAPI()

    @app.get("/health_check")
    def health_check():
        with open('setup.py', 'r') as f:
            setup_str = f.read()
        # Get version string
        version_str = _pos_string(setup_str, 'project_version=')
        # Get project string
        project_str = _pos_string(setup_str, 'project_name=')
        return {'service': project_str, 'status': '200', 'version': version_str}
    
    @app.post("/prediction", response_model=Result)
    def prediction(prediction: Prediction):
        data = {}
        data['Pclass'] = [prediction.Pclass]
        data['Sex'] = [prediction.Sex]
        data['Age'] = [prediction.Age]
        data['Fare'] = [prediction.Fare]
        data['Cabin'] = [prediction.Cabin]
        data['Embarked'] = [prediction.Embarked]
        data['Title'] = [prediction.Title]
        log.info(data)
        result = fast_api_app.prediction(data)
        return {"class_num": result[0]}

    def _pos_string(setup_str, pos_string):
        start_project_pos = setup_str.find(pos_string) + len(pos_string)
        end_project_pos = setup_str.find(',', start_project_pos)
        return setup_str[start_project_pos:end_project_pos].replace("'", '')

    return app

class Prediction(BaseModel):
    Pclass: int
    Sex: int
    Age: int
    Fare: int
    Cabin: float
    Embarked: int
    Title: int

class Result(BaseModel):
    class_num: int
