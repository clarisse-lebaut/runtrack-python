
#----------------------------------------------#
        # JOB 7 : PYRAMIDE ALPHABETIQUE #
#----------------------------------------------#

# IMPRESSION DE L'ALPHABET EN PYRAMIDE
# Une nouvelle lettre à chaque ligne
#-------------------------

chaine=("abcdefghiklmnopqrstuvwxyz")*10

P=" " #crée les espaces dans lesquelles les lettres vont appaitre

for i in chaine: 
    #pour le compteur dans la chaîne
    P = P+i
    #on indique dans P il y a i qui doit s'ajouter
    print(P) 
    #on imprime P qui va lire l'entièreté de la chaîne

#---------------------------------

print("")

# IMPRESSION DE CHIFFRE EN PYRAMIDE
# Avvancement ligne par ligne, deux chiffres 7 par deux chiffres 7
    #correspond à l'affichage comme sur la photo dans la fiche des JOB
    #je n'ai pas trouver comment le faire avec les lettres de la chaine attendu
    #soucis avec la variable ?
#-------------------------

chaine=7    
#défnit la variable
n=10
#définit le nombre de ligne
for i in range(n):
#c'est le nombre de ligne
    for j in range(i*2+1):
    #c'est le nombre de colonnes
        print(chaine, end="")#c'est un retour a la ligne
    print()