# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 15:09:02 2018

@author: buddhi

Sorts a given csv file(with headers) with respect to a given column and writes the sorted dataframe to a new csv file
"""

import pandas as pd

def sortbycol(input_file, col_name, output_file):
    df=pd.read_csv(input_file)
    df_sorted = df.sort_values(by=[col_name])
    df_sorted.to_csv(output_file, index=None)