# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 13:07:59 2022

@author: markj
"""
import numpy as np 
import matplotlib as plt 
#defining boundary conditions effects on E, the Slap is positioned -a to a hence thickness 2a

def Ei(A,k,n,z):#initial (for where z<-a)
    return (-1**n)*A*np.exp(complex(0,1)*k*z)#A is an arbitary 

def Em(B,k,n,z,ri):#middle (where -a<z<a)
    return B*(np.exp(complex(0,1)*np.sqrt(ri)*k*z)+((-1)**n)*np.exp(-complex(0,1)*np.sqrt(ri)*k*z))

def Ef(A,k,z):#final where z>a
    return A*np.exp(complex(0,1)*k*z)

    
    
def Kn(a,ri,n): #wave number eigenvalues
    alpha=(np.sqrt(ri)+1)/(np.sqrt(refracind)-1)
    return (1/(2*alpha*np.sqrt(ri)))*((np.pi*n)-complex(0,1)*np.log(alpha))

#where a is  half the dielectric slab thickness, ri is the refractive index, and n=0,1,2... etc




