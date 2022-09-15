# -*- coding: utf-8 -*-
"""Regresion_lineal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pmMaCx2Xi2DAfMvkskmfA_-iwc95Otg_
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

# %matplotlib inline

df = pd.read_excel("/content/score_cards.xlsx").drop_duplicates()# data set prueba no esta cargado pero comparto el archivo

df.info()#nombres de las columas

plt.scatter(df.IQ,df.score) # para esta prueba observamos que tiene una tendencia lineal y existe mucha cohesion
plt.show()

"""## REGRESION LINEAL"""

def regresion(mn, bn, p, l): # generamos la funcion del gradiente para la regresion
  #contadores de los gradientes
  mg = 0
  bg = 0
  lon = len(p) # calculo de la longitud de los puntos o datos
  for i in range(lon):
    x = p.iloc[i].IQ # seleccion de los datos de x de la columna IQ
    y = p.iloc[i].score # seleccion de los datos de y de la columna score
    mg += -(2/lon) * x * (y - (mn * x + bn)) #gradiente respectivo a m
    bg += -(2/lon) * (y - (mn * x * bn)) #gradiente respetivo de b 
  m = mn - mg * l # generacion de la pendiente
  b = bn - bg * l #generacion de la ordenada
  return m, b
m=0 #m inicial
b=0 #b inicial
l=0.0001 # l inicial
epocas = 1000 #numero de interaciones

"""Ejemplo de regresion"""

for i in range(epocas):
  m,b = regresion(m,b,df,l)

print("La pendiente es: "+ str(m))
print("--------------------------------------------")
print("La ordenada al origen es: " + str(b))

# Y se puede ver descrita como
print("--------------------------------------")
print("Y = " + str(m)+"*x + " + str(b))
print("--------------------------------------")

plt.scatter(df.IQ,df.score,)
plt.plot(list(range(0,110)),
         [m * x + b for x in range(0,110)], color = "red")
plt.xlabel("IQ")
plt.ylabel("Score")
plt.legend("Y")
plt.show()

x=70
Y = m*x + b # valor predecido 
print(Y)

x=68
Y = m*x + b # valor predecido 
print(Y)

#prediccion
x=40
Y = m*x + b # valor predecido 
print(Y)

"""valores esperados

![image.png](data:image/png;base64,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)
"""

def funcion_perdida(m, b, p): #generamos la funcion de perdida 
  te = 0 #contador del error total
  for i in range(len(p)):
    x = p.iloc[i].IQ # posicion de x, dentro de la columna IQ
    y = p.iloc[i].score #posicion de y, dentro de la columna score
    te +=(y - (m * x + b))**2 # calculamos el error total actulizable
  te/float(len(p)) #error total
  return te

funcion_perdida(m,b,df)