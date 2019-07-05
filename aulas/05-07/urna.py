# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 09:10:06 2019

@author: Thiago
"""

import numpy as np
import pylab as pl

'''
Lei de Zipf
'''

#gera as bolas
k=5
B = ['B'+str(i+1) for i in range(k)]

#insere as bolas na urna
U=[]
for i in range(k):
    U += [ B[i] ]

N=10000
for n in range(N): 
    #escolhe uma bola da urna
    b = np.random.choice(len(U))
    
    #insere r copias na urna
    r=3
    U += [ U[b] ]*r
        
        
#pl.hist(U)

c,y = np.unique(U, return_counts=True)
a = dict(zip(c,y))

z=1.0*y/len(U)
arg = np.argsort(z)
arg = arg[::-1]

pl.bar(c[arg],z[arg])
pl.xlabel(r'Posição'); pl.ylabel(r'Frequência')
pl.show()