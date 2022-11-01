##Definitions##

####################################Imports

import numpy as np



###############################################################################

### Wavenumber eigenvalues for homogenous 1D slab  

def Kn(a,epsilon_s,n): #wave number eigenvalues
    alpha = (np.sqrt(epsilon_s) + 1)/(np.sqrt(epsilon_s) - 1)
    return (1/(2*a*np.sqrt(epsilon_s)))*((np.pi*n) + complex(0,-1)*np.log(alpha)) 

#where a is half the dielectric slab thickness, epsilon_s is the dielectric constant
#defined for z < a, and n=+-0,+-1,+-2... etc


def An(a,epsilon_s,Kn): #Differential amplitude A_n 
    return np.exp(complex(0,-Kn*a))/np.sqrt(a*(epsilon_s-1))
# This definition calculates a single differential amplitude A_n for an nth wave number Kn.

def Bn(a, epsilon_s, n):
    return (complex(0,-1)**(n))/(2*np.sqrt(a*epsilon_s))



#defining boundary conditions effects on E, the Slap is positioned -a to a hence thickness 2a

def Ei(An,Kn,n,z):#initial (for where z<-a)
    return (-1**n)*An*np.exp(complex(0,-1)*Kn*z)#A is an arbitary 

def Em(Bn,Kn,n,z,epsilon_s):#middle (where -a<z<a)
    return Bn*(np.exp(complex(0,1)*np.sqrt(epsilon_s)*Kn*z)+((-1)**n) \
              *np.exp(complex(0,-1)*np.sqrt(epsilon_s)*Kn*z))

def Ef(An,Kn,z):#final where z>a
    return An*np.exp(complex(0,1)*Kn*z)

    
    


