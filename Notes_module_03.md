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

## 3.05 Feature Importance: Churn Rate and Risk Ratio

- A quick demonstration how one can look into data using pandas to compare if there are significant differences between the groups in the value that we are aiming to predict

## 3.06 Feature importance: Mutual inforamtion

- An interesting concept from information theory on mutual information that can give us an idea of the importance of the features
- We can easily calculate the mutual importance for the whole dataframe using an apply function in the dataframe, where, note, the passed function takes only one argument, that is the series object

## 3.07 Feature importance: correlation

- Essentially knew everything. Just useful to see that pandas offers a lot of these things easily to access. 

## 3.08 One-hot encoding on scikit-learn

- Can be done in many different ways:
    - sklearn.preprocessing.OneHotEncoder
        - Can pass dataframe directly
    - sklearn.feature_extraction.DictVectorizer
        - Have to pass a dictionary that is "rows"-like, essentially a list of dictionaries

## 3.09 Logistic regression

- Essentially this is linear regression mapped into 0 to 1. By doing linear regression and then squishing the output space using a sigmoid function (1/(1+exp(-z)))

## 3.10 Training logistic regression with Scikit-Learn

- Implemented a simple Logistic regression model on our dataset to produce a model that performs quite okay with the validation dataset.
- The important part that takes more work is actually the data preprocessing and preparation and then the visualisation or understanding of the results.

## 3.11 Model Interpretation

- Looked at the coefficients and what is their importance. Essentially, the coefficeints first a re used to produce a score and if the coefficient is +ve then it kind of means that it is promoting the positive outcome in the logistic regression and if it is negative, it is promoting the -ve outcome.
- Sigmoid function is just the last piece that helps to map from the all real number axis that the linear regression gives us, to a range (0,1), that can be used as probabilities and make decision boundaries.

## 3.12 Using the model

- Using the same model for the test dataset