import numpy as np
import matplotlib.pyplot as plt



from Definitions import An, Bn, Kn, Ei, Em, Ef

###############################################################
#### 1d slab E_n solutions for z<-a, -a<z<a and z>a


### Initialisation


epsilon_s = 1.8
a = 10**(-9)
n = 10

###


zi = np.linspace(-3*a, -a, num= 1000, endpoint = False); # z in range [-3a,-a)
zm = np.linspace(-a,a, num= 1000, endpoint = False); # z in range [-a,a)
zf = np.linspace(a,3*a, num= 1000, endpoint = True); # z in range [a,3a]


k = Kn(a,epsilon_s,n)
A = An(a,epsilon_s,k)
B = Bn(a,epsilon_s,n)

E_i = Ei(A,k,n,zi) # E_n array for z in range [-3a,-a)
E_m = Em(B,k,n,zm,epsilon_s) # E_n array for z in range [-a,a)
E_f = Ef(A,k,zf) 




plt.plot(zi, E_i,'o') # Plot E_i for -3a to -a
plt.plot(zm, E_m) # Plot E_m for -a to a
plt.plot(zf, E_f,'o') # Plot E_f for a to 3a
###############################################################################
#   Green's approach test.
