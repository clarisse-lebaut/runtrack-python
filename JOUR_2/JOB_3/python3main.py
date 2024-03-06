#----------------------------------------------#
        # JOB 3 : AFFICHAGE MASQUER #
#----------------------------------------------#

#----------------------------------------------

print(" ----- SANS BOUCLE ----- ")
#créeation d'une variable avec affichage en liste de 0 à 100
compteur = list(range (101))

#retirer les éléments 26, 37, 88 de la liste
compteur.remove(26)
compteur.remove(37)
compteur.remove(88)

#impression de cette liste
print(compteur) 

#----------------------------------------------

print(" ----- AVEC BOUCLE ----- ")
#création de la variable pour retirer
#il faut que j'indique <si x nombres est dans la liste alors n'imprime pas>
nombres=list(range(101))
for nombres in range(101):
    if nombres == 26:
        continue
    elif nombres == 37:
        pass
    elif nombres == 88:
        pass
    #else va permettre de dire <si x, x et x ne sont pas dans la liste alors tu peux imprimer>
    else:
        print(nombres)


        #if nombres not in (26, 36, 88)
        #j'aurais pu écrire ça au lieu d'écrire une ligne par chiffre