# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 08:50:32 2019

@author: Thiago
"""

import numpy as np
import pylab as pl


#%%
#
# Modelo paramétrico
#

def  profit_(P, L, R, C, H):
    return L*R*P - (H+L*C)

#%%
#
# Geração de entradas aleatorias
#

#numero de iterações
N = 10**5

P = np.random.uniform(47,   53, size=N)
L = np.random.uniform(1200, 1800, size=N)
R = np.random.uniform(0.01, 0.05, size=N)
C = np.random.uniform(0.2,  0.5, size=N)
H = 800

#%%
#
# Avaliação do modelo
#

profit = profit_(P, L, R, C, H)
#%%
#
# Loop Montecarlo
#

#%%
#
# Analise dos resultados
#

pl.hist(profit, bins=100)
pl.axvline(0, c='r',lw=3)
pl.axvline(2200, c='g',lw=3)

profit_mean = profit.mean()
pl.axvline(profit_mean, c='y',lw=3)

#profit_cum = np.cumsum(pl.histogram(profit, bins=100)[0])
#pl.plot(profit_cum, c='k')

pl.show()


print(u'Lucro médio = '+str(profit_mean))
print(u'Prob. de insucesso = '+str(sum(profit < 0)/N))
print(u'Prob. profit > 2200 = '+str(sum(profit > 2200)/N))


