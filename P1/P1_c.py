# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:43:42 2024

@author: DODI
 c. Obtenga la media, mediana, moda y geométrica; explique la diferencia de los resultados y cuál de ellas se puede utilizar en un artículo científico.
"""

import numpy as np
import pandas as pd
import statistics as st
from scipy.stats import gmean
data = pd.read_csv("original.csv")
print("la media, la mediana,la moda y geométrica")
print("La media")
print("Age\t",data["Age"].mean())
print("Sleep Duration\t",data["Sleep Duration"].mean())
print("Quality of Sleep\t",data["Quality of Sleep"].mean())
print("Physical Activity Level\t",data["Physical Activity Level"].mean())
print("Stress Level\t",data["Stress Level"].mean())
print("Heart Rate \t",data["Heart Rate"].mean())
print("Daily Steps  \t",data["Daily Steps"].mean())
print("La mediana")
print("Age\t",data["Age"].median())
print("Sleep Duration\t",data["Sleep Duration"].median())
print("Quality of Sleep\t",data["Quality of Sleep"].median())
print("Physical Activity Level\t",data["Physical Activity Level"].median())
print("Stress Level\t",data["Stress Level"].median())
print("Heart Rate \t",data["Heart Rate"].median())
print("Daily Steps  \t",data["Daily Steps"].median())
print("La moda")
print("Age",st.mode(data["Age"]))
print("Sleep Duration\t",st.mode(data["Sleep Duration"]))
print("Quality of Sleep\t",st.mode(data["Quality of Sleep"]))
print("Physical Activity Level\t",st.mode(data["Physical Activity Level"]))
print("Stress Level\t",st.mode(data["Stress Level"]))
print("Heart Rate \t",st.mode(data["Heart Rate"]))
print("Daily Steps  \t",st.mode(data["Daily Steps"]))
print("geométrica")
print("Age",gmean(data["Age"]))
print("Sleep Duration\t",gmean(data["Sleep Duration"]))
print("Quality of Sleep\t",gmean(data["Quality of Sleep"]))
print("Physical Activity Level\t",gmean(data["Physical Activity Level"]))
print("Stress Level\t",gmean(data["Stress Level"]))
print("Heart Rate \t",gmean(data["Heart Rate"]))
print("Daily Steps  \t",gmean(data["Daily Steps"]))