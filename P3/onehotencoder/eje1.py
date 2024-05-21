# -*- coding: utf-8 -*-
"""
Created on Tue May 21 01:38:39 2024

@author: DODI
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler, MinMaxScaler
from sklearn.impute import SimpleImputer

data = pd.read_csv("original.csv")

label_encoder = LabelEncoder()
data['Gender'] = label_encoder.fit_transform(data['Gender'])

print("Label Encoding:")
print(data[['Person ID', 'Gender']])