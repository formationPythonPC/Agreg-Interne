# importation des bibliothèques et constantes utiles 
import matplotlib.pyplot as plt 
import numpy as np 
from math import pi 

# déclaration des variables de l'exercice, f0, w0, A, phi
# question 2 : À COMPLÉTER
f0 = 440
w0 = 2*pi*f0
A = 3
phi = 0

# question 3 :  définition de l'intervalle d'étude : t entre 0 et 0.1 seconde
t1=np.linspace(0,0.01,100)
# ou
t2=np.arange(0,0.01,1e-4)

# question 4 : :définition de l'amplitude du signal # À COMPLÉTER 
s = A*np.sin(w0*t1+phi)

# question 5 : construction de la courbe # À COMPLÉTER
plt.plot(t1, s, color="red")

# question 6 : gestion du graphe : # À COMPLÉTER
plt.xlabel("Temps qui passe... (en secondes)")
plt.ylabel("Amplitude du signal")
plt.title("Représentation du signal $s(t)$")
# affichage
plt.show()

# question 7 : 
# On modifie t1 ou t2 pour que la discrétisation soit plus fine
# par exemple : 
#t1=np.linspace(0,0.01,1000)
## ou
#t2=np.arange(0,0.01,1e-5)

