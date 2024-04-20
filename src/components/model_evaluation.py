import sys
from src.exception import CustomException
from src.logger import logging
from typing import Tuple
from src.utils.common import get_pickle

from sklearn.metrics import accuracy_score, f1_score

class ModelEvaluationConfig:
    pass

class ModelEvaluation:
    def __init__(self):
        pass

    def evaluate(self, X, y_true, estimator = "HistGradientBoostingClassifier") -> Tuple:
        try:
            logging.info("Initiating evaluation process...")
            estimator = get_pickle(estimator = estimator)
            y_pred = estimator.predict(X)
            accuracy = accuracy_score(y_true, y_pred)
            f1 = f1_score(y_true, y_pred)

            logging.info("Evaluation on test data is evaluated...")
            logging.info(f"Accuracy: {accuracy} and f1-score: {f1}")

            return accuracy, f1
        except Exception as e:
            raise CustomException(e, sys)