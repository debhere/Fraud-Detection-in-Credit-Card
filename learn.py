import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.build_model import ModelLearning
from src.components.model_evaluation import ModelEvaluation

from src.pipeline.create_pipeline import DataPipeline
from src.exception import CustomException
from src.logger import logging




if __name__ == "__main__":
    try:
        logging.info("Lets beging the learning process...!!!")
        
        logging.info("First: data ingestion...!!!")
        di = DataIngestion()
        train, test = di.initiate_data_ingestion()

        logging.info("Starting the data transformation...!!!")
        dt = DataTransformation()
        X_train, y_train = dt.initiate_transformation(train)

        logging.info("Start pipeline creation process")
        dp = DataPipeline()
        X_train_trans = dp.build(X_train)

        logging.info("Starting model building...")
        ml = ModelLearning("HistGradientBoostingClassifier")
        score = ml.build(X_train_trans, y_train)
        #print(score)

        logging.info("Starting test data prepartion using data pipeline")
        
        y_test = test['Class']
        X_test = test.drop(columns=['Class'], axis=1)
        X_test_trans = dp.call(X_test)
        
        logging.info("Evaluating the model on test data...")

        me = ModelEvaluation()
        accuracy, f1 = me.evaluate(X_test_trans, y_test)

        print(accuracy, f1)

    except Exception as e:
        raise CustomException(e, sys)
