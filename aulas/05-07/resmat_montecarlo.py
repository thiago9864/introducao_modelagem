# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 08:32:07 2019

@author: Thiago
"""

import numpy as np
import pylab as pl

def delta(x):
    P,L,E,D = x
    return P*L**3/3./E/ (np.pi*D**4/64)
   
    
N = 100000
P = np.random.uniform(10,12,size=N)
L = np.random.uniform(1450,1550,size=N)
E = np.random.normal(70,2,size=N)
#D = np.random.normal(25,1,size=N)
D = 21+np.random.binomial(4,0.4,size=N)

X = np.c_[P,L,E,D]

Y = np.zeros(N)

for i in range(N):
    x = X[i]
    Y[i] = delta(x)
    
pl.hist(Y, bins=100)
pl.axvline(Y.mean(), c='r', lw=2)