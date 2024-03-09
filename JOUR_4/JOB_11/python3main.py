
#----------------------------------------------#
        # JOB 11 : créer et augmenter #
#----------------------------------------------#

L = [7, 11, 42, 39, 2]
print(L)
#création de la liste
ajout = len(L)
#variable qui utilise la fontion len() en tant qu'initialisation du compteur
#len() renvoie le nombre d'élément présent dans une string / une liste...
for i in range(0, ajout):
#pour i dans la liste (0 = début du compteur, ajout = variable avec len())
#range permet d'itérer une action plusieurs fois 
    L[i] = L[i]+1
    #dans liste on utilise l'index fonctionnant avec la liste
    #est égal l'index fonctionnant avec la liste + 1(qui ajoute une valeur supplémentaire au nombe que l'index trouve dans la liste)
print(L)
#augmentation de 1 pour chacun des nombres de la liste



# ----- augmentation de 1 sans la fonction len() 
L = [7, 11, 42, 39, 2]
for i in L:
        ajout = i + 1
        print(f"Avant : {i} / Après : {ajout}")
        #le print doit être dans la boucle et non pas la fermé pour pouvoir voir tous les chiffre