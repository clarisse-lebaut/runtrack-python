
#----------------------------------------------#
        # JOB 9 : Valeurs Min et Max #
#----------------------------------------------#

# -------------------------------------------
# ----- avec les fonctions max() et min()

L = [8, 24, 27, 46, 2, 16, 9, 102, 8, 84, 91]
max_value = max(L)
min_value = min(L)
print("Valeur la plus haute : ", max_value)
print("Valeur la plus basse : ", min_value)


#--------------------------------------------
# ----- avec une boucle for pour la valeur max
# --- mais celle-ci j'ai pas encore bien compris son focntionnement

L = [8, 24, 27, 46, 2, 16, 9, 102, 8, 84, 91]
max_value = None

for num in L:
    if max_value is None or num > max_value:
        max_value = num

print("La valeur maximal est :", max_value)