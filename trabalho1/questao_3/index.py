import numpy as np
import pylab as pl

nFun = 1500
k = 0.0012

r = np.zeros(1)
sum = np.zeros(1)
r[0] = 1
sum[0] = r[0]
counter = 1

while(sum[counter-1]<nFun):
    r = np.append(r,0)
    sum = np.append(sum,0)
    r[counter] = r[counter-1] + k*r[counter-1]*(nFun-r[counter-1])
    sum[counter] = sum[counter-1] + r[counter]
    print(counter,"\t",r[counter],sum[counter])
    counter = counter + 1



pl.plot(sum,'ro')
pl.show()
