# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 09:59:11 2024

@author: DODI
"""

archivo = open("original.csv")
#procedimientos obtener la columna del archivo
def columna(archivo,col):
    array=[]
    primera_linea=True
    for linea in archivo:
        if primera_linea:
           primera_linea = False  
           continue
        datos=linea.strip().split(",")
        array.append(datos[col])
    return array
vector=columna(archivo,2)
ordenado=sorted(vector)#ordenar el vector
N=len(vector)#tamaño del vector
k=3
posicion=int(N*(k/4))
c3=ordenado[posicion]
print("ultimo cuartil edad",c3,"\n el 75% de las personas tienen una edad de ",c3,"años")
archivo = open("original.csv")
vector=columna(archivo,4)
ordenado=sorted(vector)#ordenar el vector
posicion=int(N*(k/4))
c3=ordenado[posicion]
archivo = open("original.csv")
vector=columna(archivo,5)
ordenado=sorted(vector)#ordenar el vector
posicion=int(N*(k/4))
c3=ordenado[posicion]
print("ultimo cuartil Calidad del sueño",c3,"\n el 75% de las personas tienen una edad de ",c3,"años")
archivo = open("original.csv")
vector=columna(archivo,6)
ordenado=sorted(vector)#ordenar el vector
posicion=int(N*(k/4))
c3=ordenado[posicion]
print("ultimo cuartil Nievel de Actividad",c3,"\n el 75% de las personas tienen una edad de ",c3,"años")
archivo = open("original.csv")
vector=columna(archivo,7)
ordenado=sorted(vector)#ordenar el vector
posicion=int(N*(k/4))
c3=ordenado[posicion]
print("ultimo cuartil Nievel de Estres",c3,"\n el 75% de las personas tienen una edad de ",c3,"años")
archivo = open("original.csv")
vector=columna(archivo,10)
ordenado=sorted(vector)#ordenar el vector
posicion=int(N*(k/4))
c3=ordenado[posicion]
print("ultimo cuartil Polígrafo",c3,"\n el 75% de las personas tienen una edad de ",c3,"años")
archivo = open("original.csv")
vector=columna(archivo,11)
ordenado=sorted(vector)#ordenar el vector
posicion=int(N*(k/4))
c3=ordenado[posicion]
print("ultimo cuartil Pasos diarios",c3,"\n el 75% de las personas tienen una edad de ",c3,"años")
#percentil
print("-----Percentil")
archivo = open("original.csv")
vector=columna(archivo,2)
ordenado=sorted(vector)#ordenar el vector
n=80
posicion=int(N*(n/100))
c3=ordenado[posicion]
print("ultimo cuartil edad",c3,"\n el 75% de las personas tienen una edad de ",c3,"años")
archivo = open("original.csv")
vector=columna(archivo,4)
ordenado=sorted(vector)#ordenar el vector
posicion=int(N*(n/100))
c3=ordenado[posicion]
print("ultimo cuartil duracion del sueño",c3,"\n el 75% de las personas tienen una edad de ",c3,"años")
archivo = open("original.csv")
vector=columna(archivo,5)
ordenado=sorted(vector)#ordenar el vector
posicion=int(N*(n/100))
c3=ordenado[posicion]
print("ultimo cuartil Calidad del sueño",c3,"\n el 75% de las personas tienen una edad de ",c3,"años")
archivo = open("original.csv")
vector=columna(archivo,6)
ordenado=sorted(vector)#ordenar el vector
posicion=int(N*(n/100))
c3=ordenado[posicion]
print("ultimo cuartil Nievel de Actividad",c3,"\n el 75% de las personas tienen una edad de ",c3,"años")
archivo = open("original.csv")
vector=columna(archivo,7)
ordenado=sorted(vector)#ordenar el vector
posicion=int(N*(n/100))
c3=ordenado[posicion]
print("ultimo cuartil Nievel de Estres",c3,"\n el 75% de las personas tienen una edad de ",c3,"años")
archivo = open("original.csv")
vector=columna(archivo,10)
ordenado=sorted(vector)#ordenar el vector
posicion=int(N*(n/100))
c3=ordenado[posicion]
print("ultimo cuartil Polígrafo",c3,"\n el 75% de las personas tienen una edad de ",c3,"años")
archivo = open("original.csv")
vector=columna(archivo,11)
ordenado=sorted(vector)#ordenar el vector
posicion=int(N*(n/100))
c3=ordenado[posicion]
print("ultimo cuartil Pasos diarios",c3,"\n el 75% de las personas tienen una edad de ",c3,"años")
