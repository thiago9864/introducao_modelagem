# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 08:21:00 2019

@author: Thiago
"""

import pylab as pl
import numpy as np
import sympy as sp

#%%

def f_00(x, r=0.95):
    return r*x

def f_01(x, r=0.95):
    return r*(1-x)*x

#%%

n_steps = 1000
x = np.zeros(n_steps)

alpha = 0.55
x[0]=alpha
r = 3.83

for n in range(n_steps-1):
    x[n+1] = f_01(x[n], r)
    
#pl.plot(x, 'r-)
pl.plot(x, 'o', label='$r=$' + str(r))
pl.xlabel("$n$")
pl.ylabel("$x_n$")

pl.legend()
pl.show()

#%%

aux = x[int(0.95*n_steps):n_steps]
c = np.unique(aux)

t = sp.var('t')

'''
.diff = derivada
.subs = substitui uma variavel simbolica por um valor
'''

for t1 in c:
    s=f_01(t, r).diff(t).subs(t, t1)
    p = "Estavel" if abs(s) < 1 else "Instavel"
    print(t1, p)

#%%
'''
feito pelo cara do mestrado
'''
r_list = np.array([0.95, -0.90, 1.009, 3.83, 3.95, 4.0])

for r in r_list:
    
    for n in range(n_steps-1):
        x[n+1] = f_01(x[n], r)
    
    pl.figure()
    pl.plot(x, 'o', label='$r=$' + str(r))
    pl.xlabel("$n$")
    pl.ylabel("$x_n$")

pl.figure()
 
for r in r_list:
    
    for n in range(n_steps-1):
        x[n+1] = f_01(x[n], r)

    aux = x[int(0.95*n_steps):n_steps]
    c = np.unique(aux)
    
    y = []
    q = []
    for t1 in c:
        s=f_01(t, r).diff(t).subs(t, t1)
        p = "Estavel" if abs(s) < 1 else "Instavel"
        y.append(s)
        q.append(p)
        
    pl.plot(c, y, 'o-', label='$r=$' + str(r))
    pl.xlabel("$c$")
    pl.ylabel("$x_n$")
    
    for i in range(len(c)):
        pl.text(c[i], y[i], q[i])

pl.legend()
pl.show()