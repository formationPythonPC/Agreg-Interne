#-----------------------------------
# décomposition en séries de Fourier
# d'un signal carré de fréquence 440Hz
# type Arduino
#-----------------------------------

import matplotlib.pyplot as plt
import numpy as np
from math import pi

f=440
w0 = 2*pi*f
A = 5

t=np.linspace(0,0.01,1000)

#---------------------------------------------------
## avec une boucle for : 
#S=A/2
#n_infini = 200
#for n in range(0,n_infini) : 
#    s = (2*A/pi)*(1/(2*n+1))*np.sin((2*n+1)*w0*t)
#    S+=s
#---------------------------------------------------


#---------------------------------------------------
# avec une boucle while : 
#S = A/2
#n = 0
#n_infini = 200
#while n < n_infini : 
#    s = (2*A/pi)*(1/(2*n+1))*np.sin((2*n+1)*w0*t)
#    S+=s
#    n+=1
#---------------------------------------------------

#plt.plot(t,S)
#
plt.xlabel("Temps qui passe... (en secondes)")
plt.ylabel("Amplitude du signal")
plt.title("Représentation du signal $s(t)$")
plt.show()

#--------------------------
# EXERCICE SUIVANT
#--------------------------
# cas du meme signal avec T/4 en haut et 3T/4 en bas
# variation du timbre
#--------------------------

#S = A/4
#for n in range(1,200) : 
#    s = (A/(pi*n))*(np.sin(n*pi/2)*np.cos(n*w0*t) + (1-np.cos(n*pi/2))*np.sin(n*w0*t))
#    S+=s
#plt.plot(t,S)
#plt.show()




