
#----------------------------------------------#
        # JOB 7 : les multiples de 3 #
#----------------------------------------------#

L=[8, 24, 48, 2, 16]
#on demande : dans l'index de la liste L d'imprimer les nombres qui sont des multiples de 3 
for index in L:
        if index%3 ==0:
                print(f" {index} est un mutiple de trois")


#revoir cette partie parce que je comprend pas comment elle marche
#on demande : dans l'index de la liste L d'imprimer le nombre total de multiple de 3 
for index in L:
        if index == index%3:
                print(f" Il y a {index} mutiples de trois")