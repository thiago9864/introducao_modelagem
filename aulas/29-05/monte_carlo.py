# -*- coding: utf-8 -*-
"""
Created on Wed May 29 09:11:47 2019

@author: Thiago
"""
'''
Modelos estocásticos
'''

import numpy as np
import pylab as pl
import sympy as sp

#%%

def fun(x):
    return x*x

a, b, M, N = 0, 1, 1, 500
k = 0
u = np.linspace(a, b, 100)
pl.plot(u, fun(u))

for i in range(N):
    x, y = np.random.rand(2)
    pl.scatter(x, y, c='b')
    if(y<fun(x)):
        k += 1
        pl.scatter(x, y, c='r')

pl.show()     
I1 = M*(b-a)*k/N

x = sp.var('x')

I0 = sp.Integral(fun(x), (x,a,b))
display(I0, I0.evalf(), I1)

#%%

for N0 in [10, 100, 500, 1000, 5000, 50000, 100000]:
    I1=[]
    for j in range(10):
        k = 0
        for i in range(N0):
            x, y = np.random.rand(2)
            if(y<fun(x)):
                k += 1
       
        I1.append(M*(b-a)*k/N0)
        
    print(N0, np.mean(I1), np.std(I1))


#%%