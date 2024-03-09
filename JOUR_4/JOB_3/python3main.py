
#----------------------------------------------#
        # JOB 3 : ajout dans une liste #
#----------------------------------------------#

def liste():
        fruits=["pomme", "cerise", "orange"]
        fruits.append("melon")
        return fruits
print(liste())


#integrer le .append() comme instruction dans la fonction
#de manière à ce qu'il soit pris en compte dans la demande d'impression
def liste():
        ajout=[]
        fruits=["pomme", "cerise", "orange"]
        for i in fruits:
                ajout.append(i)
        # --> trouver la syntaxe / ligne de code qui perme de rajouter .append() pour avoir une valeur
                #pour le moment dans l'impression toute la liste apparait en None
        return fruits
print(f"Nouvelle liste : {liste().append("Melon")}")