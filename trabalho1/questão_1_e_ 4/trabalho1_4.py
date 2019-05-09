# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:46:31 2019

@author: gabic
"""

import  numpy as np
import pylab as pl
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt

def M1(k,n,M):
    T=np.zeros(n)
    T[0]=0
    for i in range(n):
        T[i]=T[i-1]+k*(M-T[i-1])
    return T

def M2(n,M):
    T2=np.zeros(n)
    T2[0]=0
    for i in range(n):
        T2[i]=T2[i-1]+0.001*(M-T2[i-1])**1.25
    return T2    
    
###############################################################
n=200 #numero de pontos
M=425
k=0.005 #0.005 foi o ponto que melhor funcionou

m1=M1(k,n,M)
m2=M2(n,M)
plt.plot(m1,'-',color='red')
plt.title('M1')
plt.show()

plt.plot(m2,'-',color='green')
plt.title('M2')
plt.show()
