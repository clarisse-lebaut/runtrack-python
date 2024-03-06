
#----------------------------------------------#
        # JOB 6  : LES NOMBRES PREMIERS #
#----------------------------------------------#

for nombres_premiers in range(101):
    if nombres_premiers%1 > 1:
        print(nombres_premiers)


#range(start, stop, step) = renvoie un objet place


#le prendre à l'envers ? éliminer tous les nombres de la liste qui ont plus de deux diviseur ?
        #nombre premiers = divisilbe par lui même et par 1 uniquement 
        #donc demander au programme :
                #si x nombres a plus de 2 diviseurs, pass
                #si x est divisible par lui même, print
                #si x est divisible par 1, print
                # si x est divisible par un nombre supérieur à 1, pass
                # si x par 