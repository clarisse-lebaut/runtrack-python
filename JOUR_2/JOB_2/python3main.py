
#----------------------------------------------#
        # JOB 2 : AFFICHAGE ALTERNER #
#----------------------------------------------#

#boucle qui compte les nombres de 0 à 20
#(21) ppermet de faire apparaitre le 20 car 0 est compter comme premier en info.

compteur = list(range (21))
print(compteur)
for lettre in compteur:
    print (lettre)

print(compteur[::2]) #un nombre sur deux, affiche les pairs
print(compteur[1::2]) #un nombre sur deux, affiche les impairs