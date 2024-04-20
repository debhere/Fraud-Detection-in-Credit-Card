import sys
from src.exception import CustomException
from src.logger import logging
from src.utils.common import get_basic_config, get_pickle

from typing import Tuple
from dataclasses import dataclass
import joblib

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


@dataclass
class DataPipelineConfig:
    data_pipeline:str = get_basic_config("data_pipeline")


class DataPipeline:
    def __init__(self):
        self.utils = DataPipelineConfig()
        self.pipe = Pipeline([])

    def build(self, X):
        try:
            
            logging.info("Initiating building the data pipeline")
            pipe = Pipeline(
                [
                    ('impute', SimpleImputer()),
                    ('scale', StandardScaler())
                ])
            
            data_prep = pipe.fit_transform(X)

            data_pipeline = f'{self.utils.data_pipeline}.pkl'
            joblib.dump(pipe, data_pipeline)
            self.pipe = data_pipeline

            logging.info("Data pipeline is built...")

            return data_prep

        except Exception as e:
            raise CustomException(e, sys)
        
    def call(self, X):
        try:
            data_pipeline = get_pickle()
            X_trans = data_pipeline.transform(X)
            return X_trans
        except Exception as e:
            raise CustomException(e, sys)