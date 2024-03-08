
#----------------------------------------------#
        # JOB 10 : somme d'une liste #
#----------------------------------------------#

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
#cette fonction permet de calculer tous les éléments d'une liste
def somme(L, début, fin):
    #initialisation de la somme des éléments de la liste
        total = 0
        for i in L[début:fin+1]:
                total = total + i
        return total
#on test l'algorithme
print("La somme des éléments est : ", somme(L,25,90))
#chercher pourquoi il m'affiche 0 dans le terminal 