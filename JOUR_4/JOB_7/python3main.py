
#----------------------------------------------#
        # JOB 7 : les multiples de 3 #
#----------------------------------------------#

L=[8, 24, 48, 2, 16]
#on demande : dans l'index de la liste L d'imprimer les nombres qui sont des multiples de 3 
for index in L:
        if index%3 ==0:
                print(f" {index} est un mutiple de trois")
#on demande : dans l'index de la liste L d'imprimer le nombre total de multiple de 3 
i = 0
#permet d'initialiser le compteur, à partir duquel on part de 0
for index in L:
# on dit : pour l'index dans la liste L
        if index%3 ==0:
        #si les nombres de la liste L divisé par modulo par 3 son strictement égaux à 0
                i = i + 1
                #compteur à 0 = vérifie la compatiblité de chaque chiffre de la liste avec la condition de division
print(f" Il y a {i} mutiples de trois")
#on imprime le nombre que la correspondance que le compteur à trouver
#bien placé le print sur la même ligne que le deuxieme for, pour fermer la condition, sinon l'impression n'est pas bonne

#-----------------------------------------------
# ------ avec une fonction (trouvée sur internet)

print(" ----- AVEC UNE FONCTION ----- ")

def nombreDiv(L,n):
        i = 0
        for x in L :
                if (x%n == 0):
                        i = i + 1
        return i

n=3
L=[8, 24, 48, 2, 16]
print("Le nombre d'élément de L qui sont divisible par", n, "est de", nombreDiv(L,n))


