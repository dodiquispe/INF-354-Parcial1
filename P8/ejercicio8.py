# -*- coding: utf-8 -*-
"""
Created on Mon May 20 23:13:22 2024

@author: DODI
"""
import random
grafo = {
    'Barcelona': {'Barcelona': 0, 'Bilbao': 620, 'Huelva': 1140, 'Madrid': 621, 'Málaga': 997, 'Sevilla': 1046, 'Oviedo': 902, 'Valencia': 349},
    'Bilbao': {'Barcelona': 620, 'Bilbao': 0, 'Huelva': 939, 'Madrid': 395, 'Málaga': 939, 'Sevilla': 933, 'Oviedo': 304, 'Valencia': 633},
    'Huelva': {'Barcelona': 1140, 'Bilbao': 939, 'Huelva': 0, 'Madrid': 632, 'Málaga': 313, 'Sevilla': 94, 'Oviedo': 821, 'Valencia': 791},
    'Madrid': {'Barcelona': 621, 'Bilbao': 395, 'Huelva': 632, 'Madrid': 0, 'Málaga': 544, 'Sevilla': 538, 'Oviedo': 451, 'Valencia': 352},
    'Málaga': {'Barcelona': 997, 'Bilbao': 939, 'Huelva': 313, 'Madrid': 544, 'Málaga': 0, 'Sevilla': 219, 'Oviedo': 995, 'Valencia': 648},
    'Sevilla': {'Barcelona': 1046, 'Bilbao': 933, 'Huelva': 94, 'Madrid': 538, 'Málaga': 219, 'Sevilla': 0, 'Oviedo': 789, 'Valencia': 697},
    'Oviedo': {'Barcelona': 902, 'Bilbao': 304, 'Huelva': 821, 'Madrid': 451, 'Málaga': 995, 'Sevilla': 789, 'Oviedo': 0, 'Valencia': 803},
    'Valencia': {'Barcelona': 349, 'Bilbao': 633, 'Huelva': 791, 'Madrid': 352, 'Málaga': 648, 'Sevilla': 697, 'Oviedo': 803, 'Valencia': 0}
}
ciudades = list(grafo.keys())
combinaciones = []
for _ in range(10):
    combinacion = random.sample(ciudades, len(ciudades))
    if combinacion not in combinaciones: 
        combinaciones.append(combinacion)

for combinacion in combinaciones:
    print(combinacion)
