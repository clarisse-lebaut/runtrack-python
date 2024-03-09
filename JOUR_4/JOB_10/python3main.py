
#----------------------------------------------#
        # JOB 10 : somme d'une liste #
#----------------------------------------------#

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
somme_entre_deux_valeurs = 0
#on initalise un comtpeur
for i in L:
#pour l'index (i) dans la liste L
        if i>=25 and i<=90 :
        #si un nombre de l'index est supérieur et stricemet égale à 25 ET l'index est inférieur et strictement égal à 90
                somme_entre_deux_valeurs = somme_entre_deux_valeurs + i
                #la somme entre les deux valeurs est égale à la somme des deux valeurs + i(pour que l'index cherche tout les nombres correspondand la conditio,)
print(f"La somme des nombres entre 25 et 90 est : {somme_entre_deux_valeurs}")
#imprime la somme de ces valeurs




#----------AVEC UNE FONCTION
# ----- test 1
def calcul_between():
        somme=0
        for i in L:
                if i>=25 and i<=90:
                        somme = somme + i
        return somme
        #dans le return il faut mettre le nom de la variable précédemment instauré
        #pas le i de l'index, sinon ça ne marche, la fonction ne retourne que le dernier nombre de la liste
        
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
print(f"Somme = {calcul_between()}")
#le print permet de dire ce qui doit être imprimer entre parenthèse



# ----- test 2
def calcul_between():
        somme=0
        for i in L:
                if i>=25 and i<=90:
                        somme = somme + i
        print(somme)
        #dans le return il faut mettre le nom de la variable précédemment instauré
        #pas le i de l'index, sinon ça ne marche, la fonction ne retourne que le dernier nombre de la liste
        
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
calcul_between()
#quand il y a pas le return mais un print dans les instructions de la fonction, il suffit d'appeler la fonction pour qu'elle s'imprime