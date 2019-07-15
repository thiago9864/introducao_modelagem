# -*- coding: utf-8 -*-
"""
Created on Wed May 22 08:32:24 2019

@author: Thiago
"""
import numpy as np
import pylab as pl
import sympy as sp

sp.init_printing()
#%%

x, y = sp.var('x_i, y_i') #poderia ser c_i, f_i
k = sp.var(['k_' + str(i) for i in range(4)], nonnegative = True)

u = sp.Matrix([ [x], [y] ])


F = sp.Matrix([( 1+k[0] )*x - k[2]*x*y,(1+k[1]) * y-k[3] * x*y])
        
     
J=F.jacobian(u)

p = {k[0]:0.2, k[2]:0.001, k[1]:0.3, k[3]:0.002}

solutions = sp.solve(u - F, u, dict=True)

for s in solutions:
    display(s)
    display(J.subs(s))
    P, L = J.subs(s).diagonalize()
    #display(L)
    
    for i in range(L.shape[0]):
        print('autovalor: ', i, L[i,i].subs(p))
        
#%%
        
for s in solutions:
    display(s, [i.subs(p) for i in s.values()])
    
    
#%%
    
n_steps = 30
n_var = u.shape[0]

u0 = [150, 201]
w= np.zeros((n_steps, n_var))
w[0] = u0

for i in range(0, n_steps-1):
    aux = dict(zip(u, u0))
    u0 = F.subs(p).subs(aux)
    w[i+1] = np.ravel(u0)
    
#%%
    
pl.plot(w[:,0], 'ro-', label=u'Corujas')
pl.plot(w[:,1], 'bo-', label=u'Falcões')
pl.legend()
pl.show()