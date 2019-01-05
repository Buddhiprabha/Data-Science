# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 11:17:32 2019

@author: buddhi

Input:
train_file - a CSV file containing normalized training data 
test_file - a CSV file containing normalized test data for cross validation
num_features - number of features to select 
mandatory_features - list of mandatory featues that should be present in the final feature list

Output:
Highest accuracy
The list features that gives the highest accuracy

Intermediate:
The accuracy and current feature list are printed if the current accuracy is higher than the best accuracy so far

"""

import pandas as pd
from sklearn import svm
from itertools import combinations

train_file = "depth_1_train_5000_each.csv"
test_file = "depth_1_test.csv"
num_features = 4
mandatory_features = ["QP", "homogeneity"]

df_train = pd.read_csv(train_file)
df_test = pd.read_csv(test_file)

#the column named "decision" contains the class label
test_labels = df_test["decision"]

all_features = df_train.columns[0:49]
select_from = list(set(all_features) - set(mandatory_features))
decision_column = df_train["decision"]

combs = combinations(select_from, num_features)
max_accuracy = 0
best_combination = []

for i in list(combs):
    selected_set = list(i) + mandatory_features
    y_vals = decision_column.values
    X_vals = (df_train[selected_set]).values
    
    #creating the classifier with Radial Basis Function kernal and Cost = 100
    clf = svm.SVC(kernel =  "rbf", C = 100)
    clf.fit(X_vals, y_vals)
    
    #testing against the cross-validation set
    df_test_columns_selected = (df_test[selected_set]).values
    results = clf.predict(df_test_columns_selected)
	
    num_correct = (results == test_labels).sum()
    current_accuracy = num_correct / len(test_labels)

    if (current_accuracy * 100 > max_accuracy):
        max_accuracy = current_accuracy * 100
        best_combination = selected_set
        print(max_accuracy)
        print(best_combination)
    
#finally prints the best set of features that gives the highest accuracy
print(max_accuracy)
print(best_combination)