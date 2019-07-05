# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 19:12:35 2019

@author: Thiago
"""

import numpy as np
import pylab as pl

def serie(n):
    return 1.0/((2.0*n - 1)*(2.0*n + 1))

def serie2(n):
    return 1.0/(4.0*n**2 - 1)

soma = 0

for n in range(1, 5):
    print(serie2(n))
    
for n in range(1, 100000):
    soma = soma + serie2(n)
    
    
print(soma)

'''
1/3

'''