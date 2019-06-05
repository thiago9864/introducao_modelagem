# -*- coding: utf-8 -*-
"""
Created on Fri May 31 08:25:29 2019

@author: Thiago
"""

import numpy as np
import pylab as pl
import sympy as sp

#%%

def f(x):
    return np.cos(x)

a, b, M, N0 = -np.pi/2, np.pi/2, 1, 1e6

k=0
x = np.random.uniform(a, b, size=int(N0))
y = np.random.uniform(0, M, size=int(N0))
    
for i in range(int(N0)):
    if(y[i] < f(x[i])):
        k += 1
        #pl.scatter(x, y, 'r')
    #else:
        #pl.scatter(x, y, 'b')
     
I1 = M*(b-a)*k/N0
print(I1)