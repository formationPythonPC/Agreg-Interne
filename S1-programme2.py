delta_t = 0.04
X = [0.32, 0.6, 0.88, 1.16, 1.44, 1.72]

# ........
for element in X : 
	print(element)

# calcul de la vitesse selon Ox au 4ème point
vx4 = (X[4]-X[3])/delta_t

# création d'une liste VX vide qui contiendra tous les vx
VX = []

# ...........
for i in range(len(X)-1) :
	vx = (X[i+1]-X[i])/delta_t
	VX.append(vx)

# affichage de la liste VX
# À COMPLÉTER
