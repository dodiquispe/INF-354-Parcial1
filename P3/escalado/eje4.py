# -*- coding: utf-8 -*-
"""
Created on Tue May 21 02:00:37 2024
MinMax Scaling 
@author: DODI
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler
from sklearn.impute import SimpleImputer

data = pd.read_csv("original.csv")
print(data)

numeric_features = ['Age', 'Heart Rate', 'Daily Steps']
minmax_scaler = MinMaxScaler()
data[numeric_features] = minmax_scaler.fit_transform(data[numeric_features])
print("MinMax Scaling:")
print(data[numeric_features])