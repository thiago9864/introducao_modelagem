# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 09:24:22 2019

@author: Thiago
"""

import numpy as np
import pylab as pl
import sympy as sp

sp.init_printing()

#%%

#definicao do sistema

C, B = sp.var('C_i, B_i')

u = sp.Matrix([ [C], [B] ])

k0, k1, k2, k3 = sp.var('k0, k1, k2, k3', nonnegative = True, real=True)

F = sp.Matrix([
        C + k0*C - k1*B*C,
        B - k2*B + k3*B*C
        ])

p = {k0:0.2 , k1:0.6, k2:0.6, k3:0.3 }

J=F.jacobian(u)
solutions = sp.solve(F-u, u, dict=True)

display(solutions)

#%%

#pontos fixos
'''
for s in solutions:
    display(s, [i.subs(p) for i in s.values()])
    
'''  