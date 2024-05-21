# -*- coding: utf-8 -*-
"""ejercicio4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/184_7F6odsyOg_qfjbpGBXc6YScSXCFgh
"""

from kanren import Relation, facts, run, conde, var
a = var()
# Definición de relaciones
padre = Relation()
madre = Relation()
masculino = Relation()
femenino = Relation()
# Hechos de la relación "Padres"
facts(padre, ("Juan", "Viviana"),("Carlos", "Alejandra"),("Carlos", "Judhit"))
facts(madre, ("Feliza", "Viviana"),("Viviana", "Alejandra"),("Viviana", "Judhit"))
# Hechos de la relación "masculino"
facts(masculino, ("Juan",), ("Carlos",))
# Hechos de la relación "femenino"
facts(femenino, ("Feliza",), ("Viviana",), ("Judhit",), ("Alejandra",))
print(padre.facts)
#funcion para obtener abuelos
def abuelo(x, z):
    y = var()
    return conde((padre(x, y), padre(y, z)), (padre(x, y), madre(y, z)),
                 (madre(x, y), padre(y, z)), (madre(x, y), madre(y, z)))
# Función para encontrar nietos
def nieto(x, z):
    y = var()
    return conde((padre(y, x), padre(z, y)), (madre(y, x), padre(z, y)),
                 (padre(y, x), madre(z, y)), (madre(y, x), madre(z, y)))

# Función para encontrar hermanos
def hermano(x, y):
    padre_comun = var()
    madre_comun = var()
    return conde((padre(padre_comun, x), padre(padre_comun, y), masculino(x)))

# Función para encontrar hermanas
def hermana(x, y):
    padre_comun = var()
    madre_comun = var()
    return conde((padre(padre_comun, x), padre(padre_comun, y),femenino(x)))
print("Abuelos: ",run(4, a, abuelo(a, 'Judhit')))
print("Nieto",run(2, a, nieto(a,'Feliza')))
print("Hermana",run(1, a, hermana(a, 'Judhit')))
print("Madre",run(1, a, madre(a, 'Judhit')))
print("Padre",run(1, a, padre(a, 'Judhit')))