#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 06:56:32 2021

@author: michaelmurphy
"""

import numpy as np
import pandas as pd
class OutlierFilter(object):
    """
    Takes a vector or 1D numeric array of type list, numpy array, or pandas series. 
    Returns a filtered pandas DataFrame with outliers removed and imputed with interpolated values.
    Outliers are defined as those values with a sequential difference value >=  threshold value n* (standard deviation).
    Returned DataFrame is same length as input 1D array.
    """
    
    def __init__(self, in_array):
        
        self.in_array = np.array(in_array)
        self.test_list = [1 if str(i).isnumeric() == True else 0 for i in self.in_array]
        try:
            all(self.test_list) == True
        except:
            raise ValueError
            print("Array must be numeric list, numpy array, or pandas series.")
        
    
    def view(self):
        print(self.in_array)
        
        
    def calc_diff(self):
        self.diff_array = np.diff(self.in_array, prepend=np.nan)
        return self.diff_array

           
    def interp_otlrs(self, threshold = 1):
        self.stdev = np.std(self.in_array)
        self.df_diff = pd.DataFrame(data={"d0":self.in_array, "diff0":self.calc_diff()})
        self.df_diff["d1"] = self.df_diff["d0"]
        self.df_diff.loc[self.df_diff["diff0"].abs() >= threshold*self.stdev, "d1"] = np.nan
        self.df_diff["d2"] = self.df_diff["d1"].interpolate()
        return self.df_diff
    
    def nan_otlrs(self, threshold = 1):
        self.stdev = np.std(self.in_array)
        self.df_diff = pd.DataFrame(data={"d0":self.in_array, "diff0":self.calc_diff()})
        self.df_diff["d1"] = self.df_diff["d0"]
        self.df_diff.loc[self.df_diff["diff0"].abs() >= threshold*self.stdev, "d1"] = np.nan
        return self.df_diff
        
