# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:45:39 2024

@author: DODI
   a. Con Python sin uso de librerías, calcule del ultimo cuartil, percentil 80 por columna; explique qué significa en cada caso.
   b. Realice lo mismo del inciso (a) con el uso de numpy y pandas
"""

import numpy as np
import pandas as pd
data = pd.read_csv("original.csv")
print("calcule del ultimo cuartil, percentil 80")
print("                        percentil 80","\t","cuartil 3")
print("Age                     ",np.percentile(data["Age"],80),"\t","\t","\t",np.quantile(data["Age"],0.75))
print("Sleep Duration          ",np.percentile(data["Sleep Duration"],80),"\t","\t","\t",np.quantile(data["Sleep Duration"],0.75))
print("Quality of Sleep        ",np.percentile(data["Quality of Sleep"],80),"\t","\t","\t",np.quantile(data["Quality of Sleep"],0.75))
print("Physical Activity Level ",np.percentile(data["Physical Activity Level"],80),"\t","\t","\t",np.quantile(data["Physical Activity Level"],0.75))
print("Stress Level            ",np.percentile(data["Stress Level"],80),"\t","\t","\t",np.quantile(data["Stress Level"],0.75))
print("Heart Rate              ",np.percentile(data["Heart Rate"],80),"\t","\t","\t",np.quantile(data["Heart Rate"],0.75))
print("Daily Steps             ",np.percentile(data["Daily Steps"],80),"\t","\t",np.quantile(data["Daily Steps"],0.75))

