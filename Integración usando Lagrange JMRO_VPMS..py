# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 14:30:57 2021

@author: José Manuel Ramírez Olivera.
         Viviana Paloma Muñoz Sánchez.
"""
import math as mt
import numpy as np

h=0.001
res=int(5/h)

def Lagrangeb2(x,idx,xat):
    res=np.prod([(xat-j)/(x[idx]-j) if idx!=i else 1 for i,j in enumerate(x)])
    return res

def Lagrange2(x,y,xat):
    px=sum([j*Lagrangeb2(x,i,xat) for i,j in enumerate(y)])
    return px

def Normal_Den(x):
    return (1/mt.sqrt(2*mt.pi))*mt.exp(-0.5*mt.pow(x,2))

grid=[-4+h*i for i in range(res+1)]
f_x=[Normal_Den(i) for i in grid]
P_m=[i+h/2 for i in grid]


Area=0
for i in range(len(grid)-1):
    XS=[grid[i],P_m[i],grid[i+1]]
    YS=[Normal_Den(grid[i]),Normal_Den(P_m[i]),Normal_Den(grid[i+1])]
    grid_temp=[grid[i]+j*(h/10) for j in range(10)]
    y_eval=[Lagrange2(XS,YS,k) for k in grid_temp]
    Area+=sum(y_eval)*(h/10)
print(Area)
