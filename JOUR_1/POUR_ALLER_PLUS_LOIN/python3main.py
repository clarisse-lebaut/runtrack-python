
#----------------------------------------------#
# JOB 10 : POUR ALLER PLUS LOIN -'trouve les e #
#----------------------------------------------#

#crée une variable avec la lettre 'e'
avec_le_e="le 'e' est une lettre difficilement retirable"

#crée une variable sans la lettre 'e'
sans_le_e="Jadis nous vivions sans autobus, ni taxis, ni auto"

#définir ce que le script doit trouver
lettre_a_trouver="e"

#instructions pour savoir si il y a la lettre 'e' pour la première variable avec une méthode
if lettre_a_trouver in avec_le_e:
    print("bingo, le e est présent")
if lettre_a_trouver not in avec_le_e:
    print("manqué, le e est pas présent")

#instructions pour savoir si il y a la lettre 'e' pour la première variable avec une autre méthode
#pour faire moins de répétitions dans le code
if lettre_a_trouver in sans_le_e:
    print("bingo le e est présent")
else:
    print("manqué, le e est pas présent")


""" 
on peut traduire la condition de la manière suivante :
<< si dans la variable lettre_a_trouver est dans la chaine de caractere avec_le_e
imprimer la phrase >>

 """
