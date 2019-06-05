# -*- coding: utf-8 -*-
"""
Created on Fri May 24 09:48:15 2019

@author: Thiago
"""

import numpy as np
import pylab as pl
import sympy as sp

sp.init_printing()

#%%

#definicao do sistema

x, y, z = sp.var('S_i, U_i, A_i') 

u = sp.Matrix([ [x], [y], [z] ])

alpha, beta = sp.var('alpha, beta', nonnegative = True, real=True)

F = sp.Matrix([
        0.75*x+0.20*y+0.4*z,
        0.05*x+0.60*y+0.2*z,
        0.2*x+0.20*y+0.4*z
        ])

p = {}

J=F.jacobian(u)
solutions = sp.solve(F-u, u, dict=True)

#%%

#pontos fixos

for s in solutions:
    display(s, [i.subs(p) for i in s.values()])
    
    
#%%
    
#analise de estabilidade
    
for h in solutions:
    s = h.copy()
    display(s)
    display(J.subs(s))
    P, L = J.subs(s).diagonalize()
    display(L)
    
    for i in range(L.shape[0]):
        print('autovalor: ', i, L[i,i].subs(p))
        
 
for h in solutions:
    s = h.copy()
    display(s, [i.subs(p) for i in s.values()])
       

#%%

n_steps = 23
n_var = u.shape[0]

u0 = [2222, 778, 1000]
w = np.zeros((n_steps, n_var))
w[0] = u0

for i in range(0, n_steps-1):
    aux = dict(zip(u, u0))
    u0 = F.subs(p).subs(aux)
    w[i+1] = np.ravel(u0)

for i in range(n_var):
    pl.plot(w[:,i],'o-', label=u[i])
    
pl.legend()
pl.title(u'Solução')
pl.show()
    
#%%
 
'''
n_steps = 22
n_var = u.shape[0]

for l,s in enumerate(solutions):
    u0 = [j.subs(p) for j in s.copy().values()]
    print("u0", u0)
    w = np.zeros((n_steps, n_var))
    w[0] = u0
    
    for i in range(0, n_steps-1):
        aux = dict(zip(u, u0))
        u0 = F.subs(p).subs(aux)
        w[i+1] = np.ravel(u0)
        
    for i in range(n_var):
        pl.plot(w[:,i],'o-', label=u[i])
    
    pl.legend()
    pl.title(u'Solução ' + str(l+1))
    pl.show()
    
'''