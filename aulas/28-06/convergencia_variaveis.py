# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 08:33:36 2019

@author: Thiago
"""
import numpy as np
import pylab as pl
import sympy as sp

#%%

s = 3000

for n in [100]: #[1, 2, 3, 5, 10, 200, 400]
    z=np.zeros(s);
    for k in range(n):
        x = np.random.uniform(-1,1,s)
        z += x #aqui entra funções
    y = z / np.sqrt(n)
    pl.figure(n)
    sns.distplot(y, bins=20, rug=True)
    pl.title('N = '+str(n))
    
w = np.random.normal(loc=0, scale=0.6, size=s)
pl.title('Normal')
pl.show()


#%%

import datetime as dt

a = dt.datetime(1899,12,30,23,59,59)
b = dt.datetime(1970,1,1,0,0,0)

(b-a).total_seconds()
    