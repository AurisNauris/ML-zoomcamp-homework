https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/06-trees

# 06 - Trees

## 6.01 Credit Risk Scoring Project

Getting data

## 6.02 

Looked at the data, cleaned it up and split into the train, val, and test.

## 6.03 Decision trees

- Decision tree essentially splits data based on the features. Need to control depth to avoid overfitting.
- Very useful because can easily interprete the decisions

## 6.04 Decision Tree Learning Algorithm

- Find the best split (based on criterai such as entropy or missclassification)
- Repeat on the left if STOP criteria not reached
- Repeat on the right if STOP criteria not reached

## 6.05 Decision Trees Parameters Tuning

- Running custom loops to look for the best hyperparameters
- At different hyper parameters you can get difference performance. SOmetimes though the best performance is not necessarily the best model if the slightly worse performance comes with a much simpler model