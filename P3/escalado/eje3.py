# -*- coding: utf-8 -*-
"""
Created on Tue May 21 01:58:18 2024
Standard Scaling 
@author: DODI
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import  OneHotEncoder, StandardScaler, MinMaxScaler
from sklearn.impute import SimpleImputer

data = pd.read_csv("original.csv")
print(data)
scaler = StandardScaler()
numeric_features = ['Age', 'Heart Rate', 'Daily Steps']
data[numeric_features] = scaler.fit_transform(data[numeric_features])
print("Standard Scaling:")
print(data[numeric_features])