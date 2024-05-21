# -*- coding: utf-8 -*-
"""
Created on Tue May 21 01:51:09 2024

@author: DODI
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 21 01:38:39 2024

@author: DODI
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import  OneHotEncoder, StandardScaler, MinMaxScaler
from sklearn.impute import SimpleImputer

data = pd.read_csv("original.csv")
print(data)

# Aplicar OneHot Encoding a la columna 'Sleep Disorder'
onehot_encoder_sleep = OneHotEncoder(sparse=False, handle_unknown='ignore')
sleep_disorder_encoded = onehot_encoder_sleep.fit_transform(data[['Sleep Disorder']])

# Crear un DataFrame para los datos OneHotEncoded y agregar al dataset original
sleep_disorder_df = pd.DataFrame(sleep_disorder_encoded, columns=onehot_encoder_sleep.get_feature_names_out(['Sleep Disorder']))
data = pd.concat([data, sleep_disorder_df], axis=1)

print("OneHot Encoding (Sleep Disorder):")
print(data)
