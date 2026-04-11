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

## 6.06 Ensemble Learning and Random Forest

- Ensemble learning can be applied to any model
- Ensamble model in the case of the decision trees is called a random forest; random because each decision tree is trained with a different subset of features but same number of instances. 

## 6.07 Gradient Boosting and XGBoost

- Instead of training the models independently, you train them in series by training a model and predicting the results and use the error of the model 1 prediction in the training of the model 2 training and you do that for many rounds.
- Implementation in XGBoost library

## 6.08 XGBoost Parameter Tuning

- Several hyperparamters to be tuned that improves the performance, in particular, **eta**, **max_depth**, and **min_child_weight**
- Plot the results over iterations for different combinations to look for the best performance with least complicated tree and the one that is easiest to train (depends on the end goal though)

## 6.09 Selecting the final model

- Train all the models on test data with best parameters and validate on validation dataset. CHoose hte one that is performing best and then retrain on the full train data and now only this one will be tested on the test dataset.
- In our case, the auc score from val dataset and test dataset are very similar -> did not overfit.