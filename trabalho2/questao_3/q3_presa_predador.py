# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 09:24:22 2019

@author: Thiago Almeida
"""

#import numpy as np
#import pylab as pl
import sympy as sp

sp.init_printing()

#%%


###################
##### LETRA C #####
###################


#variaveis do sistema
C, B = sp.var('C_i, B_i')

#constantes do sistema
k0, k1, k2, k3 = sp.var('k0, k1, k2, k3', nonnegative = True, real=True)


u = sp.Matrix([ [C], [B] ])

#matriz do sistema
F = sp.Matrix([
        C + k0*C - k1*B*C,
        B - k2*B + k3*B*C
        ])

#calculo dos pontos fixos
J=F.jacobian(u)
solutions = sp.solve(F-u, u, dict=True)


#mostra os pontos fixos no terminal
print("*** Pontos fixos da primeira função ***")
display(solutions)


#%%


###################
##### LETRA E #####
###################


#variaveis do sistema
C, B = sp.var('C_i, B_i')

#constantes do sistema
k0, k1, k2, k3, k4, k5 = sp.var('k0, k1, k2, k3, k4, k5', nonnegative = True, real=True)

u = sp.Matrix([ [C], [B] ])

#matriz do sistema
F = sp.Matrix([
        C + k0*C - k1*B*C - k4*C,
        B - k2*B + k3*B*C - k5*B
        ])

#calculo dos pontos fixos
J=F.jacobian(u)
solutions = sp.solve(F-u, u, dict=True)

#mostra os pontos fixos no terminal
print("\n*** Pontos fixos da segunda função ***")
display(solutions)