# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 08:29:19 2019

@author: Thiago
"""

import pylab as pl
import numpy as np
import sympy as sp
import pandas as pd
#%%

def f_00(x, r=0.95):
    return r*x

def f_01(x, r=0.95):
    return r*(1-x)*x

def f_02(x, r=0.95):
    return r*(1-x)*x-10*x**4

#%%

n_steps = 200
x = np.zeros(n_steps)

alpha = 0.55
x[0]=alpha
r = 2.83

fun = f_02

for n in range(n_steps-1):
    x[n+1] = fun(x[n], r)
    
pl.plot(x, 'ro-', label='r = '+str(r))
pl.show()
#pl.plot(x, 'r-)
'''
pl.plot(x, 'o', label='$r=$' + str(r))
pl.xlabel("$n$")
pl.ylabel("$x_n$")

pl.legend()
pl.show()
'''

#%%
'''
analise de estabilidade
'''
#r = 2.5
u = np.linspace(0,1,100)
pl.plot(u, fun(u,r), 'r-', label='r '+str(r))
pl.plot(u,        u, 'y-')

t = sp.var('t')
eq = fun(t,r) - t
sol = sp.solve(eq, t)

for s in sol:
    a = fun(t, r).diff(t).subs(t,s).evalf()
    p = u"Estável" if abs(a) < 1 else u"Instável"
    pl.plot(s,s,'o')
    pl.text(s,s,p)
    print(s,p,a)
    
pl.legend()
pl.show()


#%%
r_vector = np.linspace(1,4,100)


for r in r_vector:
    t = sp.var('t')
    eq = fun(t,r) - t
    sol = sp.solve(eq, t)
    for s in sol:
        a = fun(t, r).diff(t).subs(t,s).evalf()
        p = u"Estável" if abs(a) < 1 else u"Instável"
        print('%.3f'%r, '%.3f'%s, p)
        c = u"r" if abs(a) < 1 else u"y"
        pl.plot(r,s,c+'o')
        
pl.legend()
pl.show()

#%%



r_vector = np.linspace(1,4,100)

for r in r_vector:
    n_steps = 1000
    x = np.zeros(n_steps)
    alpha = 0.55
    x[0]=alpha

    for n in range(n_steps-1):
        x[n+1] = fun(x[n], r)
        
    x_range = range(int(0.95*len(x)), len(x))
    sol = np.unique(x[x_range])
    
    for s in sol:
        pl.scatter(r,s,s=2)

pl.xlabel('$r$')
pl.ylabel('$x^*$')     
pl.legend()
pl.show()

#%%