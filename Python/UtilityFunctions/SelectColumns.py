# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 11:40:22 2019

@author: buddhi

Selects the specified set of columns and write to a new csv file speicified by the user at output_file

Sample usage:
selectColumns("path\\to\\file\\input.csv",
              "path\\to\\file\\output.csv",
              ["contrast", "energy", "QP", "RD-cost", "Distortion", "ctuAbove-Bits", "ctuLeft-Bits", "decision"])
"""

import pandas as pd

def selectColumns(input_file, output_file, columns):
    #reading the file to pandas dataframe
    df = pd.read_csv(input_file)
    
    #create new dataframe with required columns
    df_columns_selected = (df[columns])
    
    #write the new dataframe to new csv file
    df_columns_selected.to_csv(output_file, index = 0)