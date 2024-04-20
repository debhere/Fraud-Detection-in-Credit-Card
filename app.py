import sys
from src.logger import logging
from src.exception import CustomException
from src.utils.common import get_pickle
import numpy
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)