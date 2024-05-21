# -*- coding: utf-8 -*-
"""
Created on Tue May 21 02:05:02 2024
Robust Scaling
@author: DODI
"""


import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler
from sklearn.impute import SimpleImputer

data = pd.read_csv("original.csv")
print(data)
numeric_features = ['Age', 'Heart Rate', 'Daily Steps']
robust_scaler = RobustScaler()
data[numeric_features] = robust_scaler.fit_transform(data[numeric_features])
print("Robust Scaling:")
print(data[numeric_features].head())