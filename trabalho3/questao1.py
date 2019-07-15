# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:59:59 2019

@author: Thiago
"""


import numpy as np
import pylab as pl
import statistics as st
from matplotlib.pyplot import figure

#%%

#Configuração

N_Int = [100, 1000, 10000, 100000, 1000000]
numIteracoes = 10
res = np.zeros((5,numIteracoes), dtype=np.float64)

#intervalo de integração
a, b = 0, 1.0

#maximo
M = 5



#%%


#função para integração
def f(x):
    return (np.cos(50.0*x) + np.sin(20.0*x)) ** 2

#valor exato para o intervalo [0, 1]
exato = 0.965200936050146

#cria os vetores x e y da solução da função no intervalo [0, 1]
num_pontos_sol_exata = 1000
sol_exata_x = np.zeros((num_pontos_sol_exata,), dtype=np.float64)
sol_exata_y = np.zeros((num_pontos_sol_exata,), dtype=np.float64)
x=0
delta = (b-a)/(num_pontos_sol_exata-1)
for i in range(num_pontos_sol_exata):
    sol_exata_x[i] = x
    sol_exata_y[i] = f(x)
    x += delta
    
    

#%%
#Calculo da area


for n in range(5):
    for it in range(numIteracoes):
        #quantidade de pontos
        N0 = N_Int[n]
        k=0
        #print("Executando o método de Monte Carlo com",N0,"pontos.")
        x = np.random.uniform(a, b, size=int(N0))
        y = np.random.uniform(0, M, size=int(N0))
        
        #listas que vão armazenar os pontos para geração do gráfico
        xd = []
        yd = []
        xf = []
        yf = []
        
        #contabiliza os pontos abaixo da curva e monta as listas de pontos
        for i in range(int(N0)):
            if(y[i] < f(x[i])):
                k += 1
                xd.append(x[i])
                yd.append(y[i])
            else:
                xf.append(x[i])
                yf.append(y[i])
             
        #calcula a area abaixo do gráfico
        res[n][it] = M*(b-a)*k/N0
        
        #gera um grafico para cada numero de N testado
        if(it == 0):
            #define o tamanho dos graficos
            figure(num=None, figsize=(6, 4), dpi=72, facecolor='w', edgecolor='k')

            #pontos
            pl.scatter(xf, yf, c='b', label=u'Pontos acima da curva')
            pl.scatter(xd, yd, c='g', label=u'Pontos abaixo da curva')
            
            #solução exata
            pl.plot(sol_exata_x, sol_exata_y, c='k', label=u'Solução Exata')
            
            #marca o maximo
            pl.axhline(y=M, linewidth=2, color='r', label=u'Máximo')
            
            #configura o gráfico
            pl.legend(loc='upper right')
            pl.title(u'Método de Monte Carlo com '+str(N_Int[n])+' pontos')
            pl.axis((0,1,0,6))
            pl.savefig(fname='mc_'+str(N_Int[n])+'.png', format='png')
            pl.show()

    print("Resultado com",N_Int[n],"pontos e",numIteracoes,"iterações")
    print(u'Média', st.mean(res[n]))
    print(u'Desvio Padrão', st.stdev(res[n]))