# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import pylab as pl
import numpy as np

#%%


'''
#Q: qual valor de x_0 pra que o x[16] seja 0.42?
for i in range(200):
    alpha =i/100
    x=[alpha]
    r = 0.95
    
    for n in range(17):
        aux = r*x[n]
        x.append(aux)
    
    print(alpha, x[16])
'''

#%%


for r in [0.95, -0.90, 1.009]:
    alpha = 0.55
    x=[alpha]
    
    for n in range(100):
        aux = r*x[n]
        x.append(aux)
    
    #pl.plot(x, 'r-)
    pl.plot(x, label='$r=$' + str(r))
    pl.xlabel("$n$")
    pl.ylabel("$x_n$")

pl.legend()
pl.show()
    
    
#%%


for a in range(6):
    r = a / 7.
    alpha = 0.55
    x=[alpha]
    
    for n in range(15):
        aux = r*x[n]
        x.append(aux)
    
    #pl.plot(x, 'r-)
    pl.plot(x, label='$r=$' + str(r))
    #pl.plot(x, c='green')
    pl.xlabel("$n$")
    pl.ylabel("$x_n$")

pl.legend()
pl.show()


#%%


for r in [1.5, 2.95, 3.55]:
    alpha = 0.55
    x=[alpha]
    
    for n in range(100):
        aux = r*(1.0-x[n])*x[n]
        x.append(aux)
    
    #pl.plot(x, 'r-)
    pl.plot(x, label='$r=$' + str(r))
    pl.xlabel("$n$")
    pl.ylabel("$x_n$")

pl.legend()
pl.show()