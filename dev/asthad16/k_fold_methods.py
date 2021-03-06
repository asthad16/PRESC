#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
from sklearn import model_selection
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import LeaveOneOut


# In[ ]:


def k_fold_table(model, x, y1):
    """In k-fold cross-validation, the data is divided into k folds.
    The model is trained on k-1 folds with one fold held back for testing"""
    fold = []
    mean_score = []
    for i in range(2, 21, 1):
        kfold = model_selection.KFold(n_splits=i, random_state=100)
        results_kfold = model_selection.cross_val_score(model, x, y1, cv=kfold)
        fold.append(i)
        mean_score.append(results_kfold.mean() * 100.0)
        table = pd.DataFrame(
            np.column_stack([fold, mean_score]),
            columns=["number of folds", "accuracy(mean_score(%))"],
        )
    return table


# In[ ]:


def stratified_k_fold_table(model, x, y1):
    """Stratified K-Fold approach is a variation of k-fold cross-validation that returns stratified folds,
    i.e., each set containing approximately the same ratio of target labels as the complete data.
    
    parameter are used k-neighbour=30 and weight criteria = distance by drawing conclusions 
    from hyper parameter tuning in PR mentioning #3 """
    fold = []
    mean_score = []
    for i in range(2, 21, 1):
        skfold = StratifiedKFold(n_splits=i, random_state=100)
        results_skfold = model_selection.cross_val_score(model, x, y1, cv=skfold)
        fold.append(i)
        mean_score.append(results_skfold.mean() * 100.0)
        table = pd.DataFrame(
            np.column_stack([fold, mean_score]),
            columns=["number of folds", "accuracy(mean_score(%))"],
        )
    return table


# In[ ]:


def leave_one_out_table(model, x, y1):
    """technique in which the size of the fold is “1” with “k” being set to the number of observations in the data. """
    loocv = model_selection.LeaveOneOut()
    results_loocv = model_selection.cross_val_score(model, x, y1, cv=loocv)
    return results_loocv.mean() * 100.0
