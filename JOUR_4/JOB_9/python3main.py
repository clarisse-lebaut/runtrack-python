
#----------------------------------------------#
        # JOB 9 : Valeurs Min et Max #
#----------------------------------------------#

# -------------------------------------------
# ----- avec les fonctions max() et min()

L = [8, 24, 27, 46, 2, 16, 9, 102, 8, 84, 91]
max_value = max(L)
min_value = min(L)
print(f"La valeur la plus haute est {max_value}")
print(f"La valeur la plus basse est {min_value}")


#--------------------------------------------
# ----- avec une boucle for pour la valeur max

#le none exprime l'absence de valeur, c'est un objet qui n'a aucune méthode
#la majsuscule est importante, sinon Python ne la reconnait pas
#permet de récupérer une valeur quand on ne connait pas son départ, que l'on a rien sélectionner, qu'on ne veut pas définir de valeur

L = [8, 24, 27, 46, 2, 16, 9, 102, 8, 84, 91]
max_value = None
for num in L:
        if max_value is None or num > max_value:
        #si la valeur maximum est nul ou si le num de L est supérieur à la valeur maximum définit dans la vairiable
                max_value = num
                #la valeur maximum est égale à num
print("La valeur maximal est :", max_value)

min_value = None
for num in L:
        if min_value is None or num < min_value:
        #si la valeur minimal est nul ou si le num de L est inférieur à la valeur minimum définit dans la vairiable
                min_value = num
                #la valeur minimim est égale à num
print("La valeur minimal est :", min_value)