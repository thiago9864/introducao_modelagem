# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:59:59 2019

@author: Thiago
"""


import numpy as np
import pylab as pl
import statistics as st

#%%

#função para integração
def f(x):
    return (np.cos(50.0*x) + np.sin(20.0*x)) ** 2

#valor exato para o intervalo [0, 1]
exato = 0.965200936050146

#%%

N_Int = [100, 1000, 10000, 100000, 1000000]
numIteracoes = 10
res = np.zeros((5,numIteracoes), dtype=np.float64)

#intervalo de integração
a, b = 0, 1.0

#maximo
M = 5

for n in range(5):
    for it in range(numIteracoes):
        #quantidade de pontos
        N0 = N_Int[n]
        k=0
        #print("Executando o método de Monte Carlo com",N0,"pontos.")
        x = np.random.uniform(a, b, size=int(N0))
        y = np.random.uniform(0, M, size=int(N0))
            
        for i in range(int(N0)):
            if(y[i] < f(x[i])):
                k += 1
                #pl.scatter(x, y, 'r')
            #else:
                #pl.scatter(x, y, 'b')
             
    
        res[n][it] = M*(b-a)*k/N0


    print("Resultado com",N_Int[n],"pontos e",numIteracoes,"iterações:", st.mean(res[n]))
        
