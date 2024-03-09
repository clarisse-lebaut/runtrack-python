
#----------------------------------------------#
        # JOB 4 : insérer un élément #
#----------------------------------------------#

def liste():
        fruits=["pomme", "cerise", "orange", "melon"]
        fruits.insert(2, "mangue")
        return fruits
print(liste())


#integrer le .insert() comme instruction dans la fonction
#de manière à ce qu'il soit pris en compte dans la demande d'impression
def liste():
        ajout=[]
        fruits=["pomme", "cerise", "orange", "melon"]
        for i in fruits:
                ajout.insert(0, i)
        # --> trouver la syntaxe / ligne de code qui perme de rajouter .insert() pour avoir une valeur
                #pour le moment dans l'impression toute la liste apparait en None
        return fruits
print(f"Nouvelle liste : {liste().insert(2, "mangue")}")