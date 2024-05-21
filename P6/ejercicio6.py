# -*- coding: utf-8 -*-
"""
Created on Mon May 20 21:30:15 2024

@author: DODI
"""
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import graphviz
import pandas as pd
import matplotlib.pyplot as plt

# Leer el conjunto de datos desde el archivo CSV
df = pd.read_csv("original.csv")

# Eliminar filas con valores faltantes en la columna objetivo (Sleep Disorder)
df = df.dropna(subset=["Sleep Disorder"])

# Separar las características (features) y las etiquetas (labels)
X = df.drop("Sleep Disorder", axis=1)  # Características
y = df["Sleep Disorder"]  # Etiquetas

# Convertir variables categóricas a variables dummy
X = pd.get_dummies(X)

# Entrenar un clasificador de árbol de decisión
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Generar el gráfico del árbol de decisión
dot_data = export_graphviz(clf, out_file=None, 
                     feature_names=X.columns,  
                     class_names=df["Sleep Disorder"].unique(),  
                     filled=True, rounded=True,  
                     special_characters=True)  
graph = graphviz.Source(dot_data)  

# Mostrar la imagen del árbol de decisión en una ventana emergente
graph.view()
# Mostrar la imagen del árbol de decisión en la consola
plt.show(graph)
