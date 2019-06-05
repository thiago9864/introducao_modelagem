# -*- coding: utf-8 -*-
"""
Created on Wed May 22 09:29:13 2019

@author: Thiago
"""

import numpy as np
import pylab as pl
import sympy as sp

sp.init_printing()
#%%

x, y, z = sp.var('x_i, y_i, z_i') 

u = sp.Matrix([ [x], [y], [z] ])

alpha = sp.var(['alpha_' + str(i) for i in range(2)], nonnegative = True)
gamma = sp.var(['gamma_' + str(i) for i in range(2)], nonnegative = True)
beta = sp.var(['beta_' + str(i) for i in range(3)], nonnegative = True)

F = sp.Matrix([
        (1+alpha[0])*x - gamma[0]*x*z,
        (1+alpha[1])*y - gamma[1]*y*z,
        (1- beta[0])*z + beta[1]*x*z + beta[2]*y*z,
        ])

p = {
     alpha[0]:0.15, alpha[1]:0.1, 
     gamma[0]:0.005, gamma[1]:0.002,
     beta[0]:0.25, beta[1]:0.01, beta[2]:0.01,
     }


J=F.jacobian(u)
solutions = sp.solve(u-F, u, dict=True)

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
 
'''
verificar essa celula, está com problema
'''

n_steps = 30
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
        
    
#%%