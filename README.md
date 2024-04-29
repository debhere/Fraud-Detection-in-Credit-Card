
# Fraud Detection in Credit Cards

This project is a Machine Learning implementation to detect the fradulent instances in credit card transactions.


## Authors

- [@debhere](https://www.github.com/debhere)


## Tech Stack

**Client:** HTML5, CSS

**Server:** Flask

**Machine Learning:** Scikit-Learn, Imblearn

**Data Analysis:** Numpy, Pandas, Matplotlib, Seaborn



## Dataset

The source of the dataset is kaggle https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

The dataset contains transactions made by credit cards and has almost 285,000 transactions. The datset is highly imbalanced where only 492 are fraudulent.

Moreover, apart from 'Time' and 'Amount', all other features are anonymized via PCA probably due to confidentiality issues.
## Requirements

- **Python 3.8+**
- **flask**
- **sckit-learn**
- **Numpy**
- **Pandas**
- **Matplotlib**
- **pyyaml**
- **seaborn**
- **imbalanced-learn**
- **joblib**

## Run Locally

Clone the project

```bash
  git clone https://github.com/debhere/Fraud-Detection-in-Credit-Card.git
```

Go to the project directory

```bash
  cd Fraud-Detection-in-Credit-Card
```

Create virtual environment

```bash
  conda create -p venv python=3.8 -y
```

Activate virtual environment

```bash
  conda activate venv\
```



Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python app.py
```

## Description

There are 3 main sections (if you will) of this project:-

- Model Implementation
- Front-End
- Back-end

Since , the primary objective of the project to detect the fradulent credit card transactions, the front-end and back-end are quite light-weight in nature.

### Model Implementation

*src* contains the primary source code of the entire model implmentation mechanism. The primary components are "data ingestion", "data transformation", "model building", and "model evaluation"

*pipeline* contains the data-pipeline and prediction-pipeline.

*utils* directory comprises of common utility functions that is being referred throughout the project.

The starting point of the "model implemention" module is learn.py where each component is being invoked one by one ie., 

data ingestion -> data transformation -> pipeline creation -> model building -> model evaluation.

The best estimator and data pipeline are saved as pickle files as artifacts.

### Front-End

Front-end is nothing but a playground of the model output. Although the majority of the features are anonymized but still thought to create a light-weight interface to demonstrate the usability.

index.html is the solitary html page here with basic css in place.

### Back-End

The back-end server should be kept light-weight for obvious reasons. app.py is the starting point to run the flask server. Once the server is up and running, user will be able to input data onto the front-end html page. flask server captures and performs the data transformation and prediction by invoking the prediction pipeline module. Thereafter, the prediction is rendered on the same UI.

## Support

For any query or discussion, email debmalya.mondal@outlook.com or send me a message on 

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/debmalyamondal)

