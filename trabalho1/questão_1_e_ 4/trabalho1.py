# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:39:14 2019

@author: gabic
"""

import  numpy as np
import pylab as pl
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
import math as mt

#rendimento é o valor novo menos o valor anterior
def rendimento(P,i,n):
    aux=np.zeros(n, np.float64)
    r=np.zeros(n, np.float64)
    for a in range(n):
        aux[a]=P[a]*i
    r[0]=aux[0]    
    for a in range(n):
        if(a!=0):
            r[a]=aux[a]-aux[a-1]
    return r    
    
#vou ter que retornar um montante de cada mes
def montante(P,i,n):
    M=np.zeros(n,np.float64)
    for a in range(len(P)):
        M[a]=P[a]*((i+1)**n)
    
    return M

        

i=0.005 #taxa por mes
n=60 #5 anos tem 60 meses    
P=np.zeros(n,np.float64)
P[0]=5000
for a in range(len(P)):
    if(a!=0):
        P[a]=P[a-1]+200 #P é meu valor inicial dividido por mes
for a in range(len(P)):
    print(P[a])
    
    
m=montante(P,i,n)
print(m)
rendimento=rendimento(P,i,n)
print(rendimento)
plt.plot(m,'-',color='red')
plt.xlabel('meses')
plt.ylabel('Montante')
plt.show()


plt.plot(rendimento,'-',color='green')
plt.xlabel('Meses')
plt.ylabel('Rendimento')
plt.show()

   