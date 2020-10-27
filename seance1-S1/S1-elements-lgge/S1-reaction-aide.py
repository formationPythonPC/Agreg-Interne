###############################
## 2 H2S + SO2 ---> 3 S + 2 H2O
###############################

#########################################################
## question 1 : valeur des coefficients stoechiométriques
#########################################################

coeff_H2S = 2 # coefficient stoechiométrique de H2S

# À COMPLÉTER : Entrez les autres coefficients



##############################################
## question 2 : quantités de matière initiales
##############################################
# on demande à l'utilisateur la quantité de H2S initiale
n0_H2S = input("Donne le nombre de moles de H2S : ")
# on transforme cette donnée (typée chaîne de caractères) en nombre décimal
n0_H2S = float(n0_H2S)

# À COMPLÉTER : faites de même pour les autres espèces ;
# pouvez-vous condenser les 2 lignes en une ?





###############################################
## question 3 : calcul des avancements maximaux
###############################################
xmax_H2S = n0_H2S/coeff_H2S

# À COMPLÉTER : faites de même pour SO2





#################################################
## question 4 : avancement maximal de la réaction
#################################################

# À COMPLÉTER : 
# on utilise une condition pour trouver l'avancement maximal de la réaction :
# si le xmax de H2S est plus petit (ou égal) que le xmax de SO2
# alors xmax de la réaction vaut xmax de H2S
# sinon, xmax de la réaction vaut xmax de SO2






#on aurait aussi pu utiliser la fonction min :
# xmax = min(xmax_H2S, xmax_SO2)




# À COMPLÉTER : on affiche le résultat sous la forme xmax = ..... mol



#######################################################
## question 5 : calcul des quantités de matière finales
#######################################################
# on calcule les quantités de matière finales en fonction
#des quantités initiales, des différents coeffs et de l'avancement maximal
nF_H2S = n0_H2S - coeff_H2S*xmax

# À COMPLÉTER : faites de même pour les autres espèces de la réaction




# À COMPLÉTER : on les affiche sur la console
# sous la forme nF_xxxx = ...... mol.
