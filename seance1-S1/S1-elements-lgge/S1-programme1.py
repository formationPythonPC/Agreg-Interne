# importation des bibliothèques utiles
import matplotlib.pyplot as plt
import numpy as np
# définitions des variables utiles
A0 = 4
landa = 0.5 # lambda est un mot réservé en python : on ne peut l'utiliser comme variable
omega = 6
phi = 0

# définitions des grandeurs à décrire
T = np.arange(0.1,10,0.025)
A = A0*np.exp(-landa*T)*np.sin(omega*T+phi)

# sortie console
print(T[2], " --- ", A[2])

# Construction de la courbe
plt.plot(T,A, color="red")

# Autres définitions
plt.title("Oscillateur harmonique amorti")
plt.xlabel("temps")
plt.ylabel("Amplitude")
plt.grid()

# affichage de la courbe
plt.show()

