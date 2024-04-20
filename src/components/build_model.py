import sys
import joblib
from typing import Dict
from src.exception import CustomException
from src.logger import logging
from src.utils.common import get_basic_config, get_model_params

from sklearn.model_selection import GridSearchCV
from imblearn.over_sampling import SMOTE
from dataclasses import dataclass

@dataclass
class ModelLearningConfig:
    model_path:str = get_basic_config("model")

class ModelLearning:
    def __init__(self, model:str):
        self.utils = ModelLearningConfig()
        self.model = model

    @staticmethod
    def _model_params(model_name:str):
        if model_name != "all":
            model, params = get_model_params(model_name)
            return model, params
    
    def build(self, X, y) -> Dict:
        try:
            logging.info("Model fitting initiated...!!!")
            model, params = self._model_params(self.model)

            scoring = ['accuracy', 'f1']

            grid = GridSearchCV(
                estimator = model,
                param_grid = params,
                scoring = scoring,
                refit = 'f1',
                n_jobs = -1,
                cv = 3
            )
            
            grid.fit(X, y)
            estimator = grid.best_estimator_
            joblib.dump(estimator, f'{self.utils.model_path}_{self.model}.pkl')

            logging.info("Model fitting is completed...")

            logging.info(grid.cv_results_)

            return grid.cv_results_

        except Exception as e:
            raise CustomException(e, sys)import sys
import joblib
from typing import Dict
from src.exception import CustomException
from src.logger import logging
from src.utils.common import get_basic_config, get_model_params

from sklearn.model_selection import GridSearchCV
from imblearn.over_sampling import SMOTE
from dataclasses import dataclass

@dataclass
class ModelLearningConfig:
    model_path:str = get_basic_config("model")

class ModelLearning:
    def __init__(self, model:str):
        self.utils = ModelLearningConfig()
        self.model = model

    @staticmethod
    def _model_params(model_name:str):
        if model_name != "all":
            model, params = get_model_params(model_name)
            return model, params
    
    def build(self, X, y) -> Dict:
        try:
            logging.info("Model fitting initiated...!!!")
            model, params = self._model_params(self.model)

            scoring = ['accuracy', 'f1']

            grid = GridSearchCV(
                estimator = model,
                param_grid = params,
                scoring = scoring,
                refit = 'f1',
                n_jobs = -1,
                cv = 3
            )
            
            grid.fit(X, y)
            estimator = grid.best_estimator_
            joblib.dump(estimator, f'{self.utils.model_path}_{self.model}.pkl')

            logging.info("Model fitting is completed...")

            logging.info(grid.cv_results_)

            return grid.cv_results_

        except Exception as e:
            raise CustomException(e, sys)