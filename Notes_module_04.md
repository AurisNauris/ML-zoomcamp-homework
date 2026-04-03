https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/04-evaluation

# 4 Evaluation

## 4.01 Overview

- Accuracy vs other evaluation metrics
- Setting up the notebook - needed to update the code a bit because pandas 'object' selector didn't work for 'str'

## 4.02 Accuracy and dummy model

- Not appropriate to use accuracy when you have a class imbalance, because just guessing the most common category, will give you accuracy equal to the fraction of that class.

## 4.03 Confusion matrix

- Revisited the confusion table with metrics of True positive, True negative, False positive, and False negative, established how to calculate them
- Useful part to imagin the whole set as a circle and draw two decision boundaries, giving rise to usually 4 regions of interest.