https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/04-evaluation

# 4 Evaluation

## 4.1 Overview

- Accuracy vs other evaluation metrics
- Setting up the notebook - needed to update the code a bit because pandas 'object' selector didn't work for 'str'

## 4.2 Accuracy and dummy model

- Not appropriate to use accuracy when you have a class imbalance, because just guessing the most common category, will give you accuracy equal to the fraction of that class.