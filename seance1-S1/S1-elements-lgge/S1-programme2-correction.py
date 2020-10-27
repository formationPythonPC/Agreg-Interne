delta_t = 0.04
X = [0.32, 0.6, 0.88, 1.16, 1.44, 1.72]

# on fait afficher les éléments de la liste X
for element in X : 
	print(element)

# calcul de la vitesse selon Ox au 4ème point : cohérent avec la définition
# X[4] est le 5ème élément de la liste (python numérote à partir de 0
# X[3] est le 4ème élément de la liste (python numérote à partir de 0
vx4 = (X[4]-X[3])/delta_t

# création d'une liste VX vide qui contiendra tous les vx
VX = []

# calcul de tous les vxi des différents points (sauf le dernier)
# et placement dans une liste VX
for i in range(len(X)-1) :
	vx = (X[i+1]-X[i])/delta_t
	VX.append(vx)

# affichage de la liste VX
print(VX)
