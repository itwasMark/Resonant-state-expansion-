# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 13:07:59 2022

@author: markj
"""
import numpy as np 
import matplotlib as plt 

def Kn(a,ri,n): #wave number eigenvalues
    alpha=(np.sqrt(refracind)+1)/(np.sqrt(refracind)-1)
    return (1/(2*alpha*np.sqrt(refracind)))*((np.pi*n)-complex(0,1)*np.log(alpha))

#where a is dielectric slab thickness, ri is the refractive index, and n=0,1,2... etc


