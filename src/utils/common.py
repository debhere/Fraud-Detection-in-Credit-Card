import sys
from src.exception import CustomException
from src.logger import logging
import yaml
import os
import joblib
from typing import Tuple, Any

from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier


def get_basic_config(param:str)-> str:
    """
        This is a common utility function used to fetch the base config parameters

    Parameter:
        The function parameter should be of string type and 
        the permissible parameters are:
        raw, train, test, data_pipeline, model

    Return:
        return type is string
    """
    try:
        param_path:str = None
        logging.info("loading the base config")
        
        with open("config/basic.yaml") as f:
            basic_config = yaml.safe_load(f)

            if param == "train" or param == "test":
                os.makedirs(basic_config["artifacts_folder"], exist_ok=True)
                file_name = basic_config[param]
                param_path = os.path.join(basic_config["artifacts_folder"], file_name)
            elif param == "data_pipeline":
                param_path = os.path.join(basic_config["artifacts_folder"], basic_config["data_pipeline"])
            elif param == "model":
                param_path = os.path.join(basic_config["artifacts_folder"], basic_config["model"])
            else:
                param_path = os.path.join(basic_config["data_folder"], basic_config["data_file"])

        return param_path

    except Exception as e:
        raise CustomException(e, sys)
            

def get_model_params(*args:str) -> (Any | Tuple):
    """
    build it in a better way tomorrow
    """
    try:
        logging.info("Fetching model params...")
        model_config:tuple = None, None
        with open('config/param.yaml') as f:
            all_config:dict = yaml.safe_load(f)
        
        for arg in args:
            if arg == "RandomForestClassifier":
                rf = RandomForestClassifier()
                params = all_config[arg]
                model_config = rf, params
            elif arg == "HistGradientBoostingClassifier":
                hgb = HistGradientBoostingClassifier()
                params = all_config[arg]
                model_config = hgb, params
            elif arg == "KNeighborsClassifier":
                knc = KNeighborsClassifier()
                params = all_config
                model_config = knc, params
            elif arg == "all":
                return all_config
            else:
                return None
        
        return model_config

    except Exception as e:
        raise CustomException(e, sys)

def get_pickle(estimator=None):
    try:
        pickle_path = None
        if estimator is not None:
            pickle_path = joblib.load(f'artifacts/model_{estimator}.pkl')
        if estimator is None:
            pickle_path = joblib.load('artifacts/data_pipeline.pkl')

        return pickle_path
    except Exception as e:
        raise CustomException(e, sys)
        
