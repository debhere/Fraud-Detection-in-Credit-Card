
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

- **Python 3.11**
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

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python app.py
```

Run the playground (on browser)

```
   http://locahost:5000 
```

## Description

There are 4 main modules (if you will) of this project