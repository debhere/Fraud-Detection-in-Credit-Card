import sys
from src.exception import CustomException
from src.logger import logging
from src.utils.common import get_basic_config
from typing import Tuple

from dataclasses import dataclass

import pandas as pd
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    data_file:str = get_basic_config("raw")
    train_file:str = get_basic_config("train")
    test_file:str = get_basic_config("test")
  

class DataIngestion:
    def __init__(self):
        self.utils = DataIngestionConfig()

    def initiate_data_ingestion(self)-> Tuple:
        try:
            logging.info("Initiating data ingestion")
            raw = self.utils.data_file
            df = pd.read_csv(raw)

            train, test = train_test_split(df, test_size=0.2)

            train.to_csv(self.utils.train_file, index=False, header = True)
            test.to_csv(self.utils.test_file, index=False, header = True)

            logging.info("Data ingestion is completed")


            return (
                train, test
            )

        except Exception as e:
            raise CustomException(e, sys)