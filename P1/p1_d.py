# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 17:10:14 2024

@author: DODI
   d. Grafique los datos y explique su comportamiento (PYTHON)
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("original.csv")
df = pd.DataFrame(data)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Age', y='Sleep Duration')
plt.title('Edad vs. Duración del Sueño')
plt.xlabel('Edad')
plt.ylabel('Duración del Sueño')
plt.show()
#ocupacion vs nivel de estres
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Occupation', y='Stress Level')
plt.title('Ocupación vs Nievel de estrés')
plt.xlabel('Ocupación')
plt.ylabel('Nivel de Estrés')
plt.show()
#Agevs Sleep Disorder
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Sleep Disorder', y='Age')
plt.title('Edad vs Desorden del Sueño')
plt.xlabel('Edad')
plt.ylabel('Desorden del sueño')
plt.show()
#edadn vs nivel de estres
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Age', y='Stress Level')
plt.title('Edad vs Nievel de estrés')
plt.xlabel('Edad')
plt.ylabel('Nivel de Estrés')
plt.show()