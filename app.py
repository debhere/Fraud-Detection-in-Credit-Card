import sys
from src.logger import logging
from src.exception import CustomException
from src.utils.common import get_pickle
import numpy as np
from flask import Flask, render_template, request
from src.pipeline.prediction_pipeline import PlaygoundData, PredictPipeline

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    try:
        pg = PlaygoundData(
            time = float(request.form.get('time')),
            V1 = request.form.get('v1', type = float, default=np.nan),
            V2 = request.form.get('v2', type = float, default=np.nan),
            V3 = request.form.get('v3', type = float, default=np.nan),
            V4 = request.form.get('v4', type = float, default=np.nan),
            V5 = request.form.get('v5', type = float, default=np.nan),
            V6 = request.form.get('v6', type = float, default=np.nan),
            V7 = request.form.get('v7', type = float, default=np.nan),
            V8 = request.form.get('v8', type = float, default=np.nan),
            V9 = request.form.get('v9', type = float, default=np.nan),
            V10 = request.form.get('v10', type = float, default=np.nan),
            V11 = request.form.get('v11', type = float, default=np.nan),
            V12 = request.form.get('v12', type = float, default=np.nan),
            V13 = request.form.get('v13', type = float, default=np.nan),
            V14 = request.form.get('v14', type = float, default=np.nan),
            V15 = request.form.get('v15', type = float, default=np.nan),
            V16 = request.form.get('v16', type = float, default=np.nan),
            V17 = request.form.get('v17', type = float, default=np.nan),
            V18 = request.form.get('v18', type = float, default=np.nan),
            V19 = request.form.get('v19', type = float, default=np.nan),
            V20 = request.form.get('v20', type = float, default=np.nan),
            V21 = request.form.get('v21', type = float, default=np.nan),
            V22 = request.form.get('v22', type = float, default=np.nan),
            V23 = request.form.get('v23', type = float, default=np.nan),
            V24 = request.form.get('v24', type = float, default=np.nan),
            V25 = request.form.get('v25', type = float, default=np.nan),
            V26 = request.form.get('v26', type = float, default=np.nan),
            V27 = request.form.get('v27', type = float, default=np.nan),
            V28 = request.form.get('v28', type = float, default=np.nan),
            amount = request.form.get('amount', type = float, default=np.nan)
        )
        
        df = pg.formulate()
        
        logging.info("Playground data is formatted...!!")
        logging.info(df)

        logging.info("Predict on the basis of user data...")
        predict_pipeline = PredictPipeline()
        prediction = predict_pipeline.get_prediction(df)

        status = "valid" if prediction == 0 else "fraud"
        #prediction_text = "The client is probably a"
        return render_template('index.html', 
                               prediction_text = f"The credit card transaction is {status}")

    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    app.run(debug=True)