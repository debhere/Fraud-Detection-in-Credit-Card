import sys
from src.logger import logging
from src.exception import CustomException
from src.utils.common import get_basic_config
from dataclasses import dataclass
from typing import Tuple

@dataclass
class DataTransformationConfig:
    data_pipeline_path:str = get_basic_config("data_pipeline")

class DataTransformation:
    def __init__(self):
        self.utils = DataTransformationConfig()
    
    def initiate_transformation(self, train_df) -> Tuple:
        try:
            
            logging.info("Initiating data transformation!!!!")
            df = train_df.drop_duplicates()
            
            y_train = df['Class']
            X_train = df.drop(columns=['Class'], axis=1)

            logging.info("Training data transformation completed!!!!")

            return (X_train, y_train)


        except Exception as e:
            raise CustomException(e, sys)