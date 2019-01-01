# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 20:59:14 2018

@author: buddhi

Selects the rows that have a given value for a column and writes the rows to a new csv
"""

import pandas as pd

def selectByColVal(input_file, output_file, value, col_name):
    df = pd.read_csv(input_file)
    df_depth1_extracted = df[df[col_name]==value]
    df_depth1_extracted.to_csv(output_file, index=None)
             