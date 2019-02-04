# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 13:49:15 2019

@author: buddhi
"""

"""
This method calculates the F-score for each feature in a given CSV file.
Can be used to determine the importance of a given feature.
This method is written for 2-class classification with classes 1 and 0.

Pass in the input file - a csv containing all features as columns
            and column name that has the classification decision
            
Sample usage (if the column header of the decision column is "decisionClass")
calc_f_score(<path_to_file>, "decisionClass")
            
NOTE: the method is not optimized
"""

import pandas as pd

def calc_f_score(in_file, decision_col):
    df = pd.read_csv(in_file)
    
    df_pos = df[df[decision_col]==1]  #extract positive columns
    df_neg = df[df[decision_col]==0]  #extract negative columns
    
    for column in df:
    
        col_sum = (df[column]).sum()  #sum of current column for all
        col_tot_elem = df[decision_col].count()
        
        pos_sum = (df_pos[column]).sum()    #sum of current column for positive instances    
        neg_sum = (df_neg[column]).sum()    #sum of current column for negative instances
        
        col_pos_elem = df_pos[decision_col].count()  #number of pos elements
        col_neg_elem = df_neg[decision_col].count()  #number of neg elements
        
        tot_avg = col_sum / col_tot_elem
        pos_avg = pos_sum / col_pos_elem
        neg_avg = neg_sum / col_neg_elem
        
        sum_pos_sq = 0
        sum_neg_sq = 0
        
        df_pos_curr = df_pos[column]
        df_neg_curr = df_neg[column]
        
        for row in df_pos_curr:
            sum_pos_sq = sum_pos_sq + ( (row-pos_avg)*(row-pos_avg) )
    
        for row in df_neg_curr:
            sum_neg_sq = sum_neg_sq + ( (row-neg_avg)*(row-neg_avg) )
            
        sum_pos_sq_avg = sum_pos_sq / (col_pos_elem - 1)
        sum_neg_sq_avg = sum_neg_sq / (col_neg_elem - 1)
        
        #fitting in the values to the F-score formula
        f_score = ((pos_avg - tot_avg)  * (pos_avg - tot_avg) + (neg_avg - tot_avg) * (neg_avg - tot_avg)) / (sum_pos_sq_avg + sum_neg_sq_avg)
        print(column," , ",f_score)