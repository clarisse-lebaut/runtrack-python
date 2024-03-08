
#----------------------------------------------#
        # JOB 5 : calcul de remplpacement #
#----------------------------------------------#


L=[1, 2, 3, 4, 5]

print(L)
#impression de la liste
print(L[1])
#impression du 2 en allant chercher la deuxième valeur de la liste

#fonction pour remplacer la smme
def remplace():
        L[3]=L[2]+L[4]
        #on dit que la valeur trois est égal a la valeur 2 + à la valeur 4
        print(L)
        #on demande d'imprimer cette liste
remplace()
#on demande d'imprimer cette liste

print(L[-1])
#impression de la dernière valeur de la liste





"""
def remplace():
        for L[3] in L:
                return(L[2]+L[4])
print(L,remplace())
"""