https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/

# 2 - Regression

## 2.01 - Car Price Intro

- Data will be used from kaggle
https://www.kaggle.com/datasets/CooperUnion/cardataset

## 2.02 - Data Preparation

- Made small changes to the string entries

## 2.03 - Exploratory Data Analysis

- Long tail distributions confuse models. It is best when we have more normal-like distributions. For that, we can use non-linear functions that compress values, e.g. logarithm is one such function

## 2.04 - Setting up the validation framework

- Used basic numpy and pandas to perform shuffling and splitting of our data into train, val, and test datasets

## 2.05 - Linear regression

- A basic linear regression formula shown and how to implement a calculation of the linear function in python

## 2.06 - Linear regression: Vector form

- A quick walk through how to set-up linear regression formula itself in matrix and vector form

## 2.07 - Training a linear regression model

- Implemented linear regression using an approximation solution by using the solution from the linear algebra with Gramm matrix

## 2.08 Car price baseline model

- A simple model seems to be doing okayish just by plotting histograms

## 2.09 RMSE

- Implemented custom computation RMSE calculation

## 2.10 Computing RMSE on validation data

- The RMSE for the validation dataset was computed. Error similar to the training dataset

## 2.11 Feature engineering

- With numerical features, such as year, one could transform that feature into something like ('age') that may be better suited for the ML model
- When I created a new feature 'age' and kept the old one 'year' without any standardisation, the prediction went wild. My guess it is the correlation issue.

## 2.12 Categorical variables

- Categorical values that are string representations usually but not always, can be often efficiently encoded as a feature for machine learning applications using a hot-ones encoding. This can be done easily on tabular table using pandas directly.
- Creating a lot of features will definitely need regularisation to keep the model from going weird

## 2.13 Regularisation

- In a linear regression model, one simple way to regularise the model is to add a small number to the diagonal values of the Gramm matrix. This can be done by adding a scaled np.eye() matrix of the same shape as Gramm matrix.
- Generally helps to reduce numerical issues with invertability

## 2.14 Tuning the model

- Ran a check with several different values of regularisation parameter to see how it affects our model
- Found that many of them give very similar results but even a tiny bit of regularisation helps significantly

## 2.15 Using the model

- The model after training can be used then to predict prices etc on a single sample basis
- The series has shown how to preprocess data and perform feature engineering. There was a mistake in how it is deal with that turned into a small learning experience. Essentially, using unique entries from the whole dataframe for feature engineering may not work well if it is directly applied to a single entry, because it has a single unique value in, say, category make, instead of expected 5. This may also lead to a problem if the the most common unique values are slightly different in train, val, or test datasets.
- It is kind of good when there are mistakes and things don't work because then you need to dig a bit deeper to understand a bit more.