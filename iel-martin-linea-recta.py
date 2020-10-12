# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 20:13:53 2020

@author: José-Manuel Martin Coronado (IEL)
"""

"1) Ecuación:Y = a+b*X para n y para N"

n = 30
N = 100

a = 10
b = 4

import numpy as np

x1 = np.array(list(range(1,n+1,1)))

y = a+b*x1

'2) Gráfico'

import matplotlib.pyplot as plt
plt.plot(x1,y)
plt.ylabel('Variable Y')
plt.xlabel('Variable X')
#plt.show()


'3) Perturbación aleatoria'

ey = sum(y)/n

sdy = (sum((y-ey)**2)/(n-1))**0.5

e = np.random.randint(-sdy/2,sdy/2,n)

y2 = y+e

plt.plot(x1,y2)
plt.ylabel('Variable Y2')
plt.xlabel('Variable X')
plt.plot(x1,y)

'3) Regresión lineal (matricial)'

x1.shape = (n,1)
y.shape = (n,1)
y2.shape = (n,1)


i = np.full((1,n),1)
type(i)
i.shape = (n,1)
i

x = np.column_stack([i,x1])
type(x)
x.shape

print(x)

xt = np.transpose(x)
xt

xx = xt@x
xx

invxx = np.linalg.inv(xx)

betas = invxx@xt@y2

y3 = betas[0]+betas[1]*x1


plt.plot(x1,y2)
plt.ylabel('Variable Y2')
plt.xlabel('Variable X')
plt.plot(x1,y)
plt.plot(x1,y3)
