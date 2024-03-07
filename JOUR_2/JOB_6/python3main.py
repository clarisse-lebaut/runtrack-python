
#----------------------------------------------#
    # JOB 6 : LES NOMBRES PREMIERS #
#----------------------------------------------#

# écrire un programme qui affiche les nombres premiers jusqu'a 1000
# 1 n'est pas un nombre premier dans tous les cas
#fonction qui permet de tester si un nombre est premier ou non
def nombrePremier(number):
    # n prend les valeurs de 2 a number
    for n in range (2,number):
        # % modulo renvoie le reste de la division euclidienne ou entière
        if number % n ==0:
            #renvoyer si le nombre est pas premier
            return False
    #renvoyer si le nombre est premier 
    return True

#dans ce print on est essaie le renvoie de la valeur du nombre présent entre parenthèse
"""print(nombrePremier(13))""" #en commentaire pour ne pas avoir le true / false qui s'affiche en console
#le chiffre entre parenthèse correspond au mot number écrit plus haut

#ici on test sur plusieurs chiffre, pas uniquement sur la ligne précédente
#faire appel a number pas a x, meme si je sais pas trop a quoi est égal x dans for 
#si a la place de number je met x, alors c'est que le x fais appel a la variable crée dans la fonction 
for number in range(2, 1001):
    if nombrePremier(number):
        print(number)



""" résumé de ce que je viens de faire :"""
""" on a d'abord définit une fonction 
    qui définit ce qu'est un nombre premier
    puis on lui a dit dans une boucle dans laquelle 
    """

#-------------------------------------------
#------------------------------ VU EN HOW-TO

for nombre in range(0, 1001):
    if nombre > 1:
        for index in range(2, nombre):
            if (nombre % index) == 0:
                break
        else:
            print(nombre)

""" notre boucle commence en fonction de nombre donnée dans le range dans la première ligne """