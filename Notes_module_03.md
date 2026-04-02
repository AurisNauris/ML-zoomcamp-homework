https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/03-classification

# 3 - Classification

## 3.01 - Churn project 

- We will use scikit-learn logistic regression to predict whether a person leaves our services.
- Dataset: https://www.kaggle.com/blastchar/telco-customer-churn
- CSV: https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-03-churn-prediction/WA_Fn-UseC_-Telco-Customer-Churn.csv

## 3.02 = Data Preparation

- Loaded data and updated some things, like the y column, processed from yes/no to 1/0

## 3.03 Setting up the validation framework

- Prepared a train, val, and test datasets using sklearn.model_selection.train_test_split
- Prepared target values and feature dataframes

## 3.04 Exploratory data analysis

- Quickly checked about which columns are numeric and which ones are categorical. Also looked at the number of unique values in the categorical ones.

