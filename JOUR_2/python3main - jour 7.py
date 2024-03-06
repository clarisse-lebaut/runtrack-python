
#----------------------------------------------#
    # JOB 7  : PYRAMIDE ALPHABIETIQUE #
#----------------------------------------------#

chaine=("abcdefghiklmnopqrstuvwxyz")*10

P=" " #crée les espaces dans lesquelles les lettres vont appaitre

for i in chaine: 
    #pour le compteur dans la chaîne
    P = P+i
    #on indique dans P il y a i qui doit s'ajouter
    print(P) 
    #on imprime P qui va lire l'entièreté de la chaîne