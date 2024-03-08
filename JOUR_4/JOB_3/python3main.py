
#----------------------------------------------#
        # JOB 3 : ajout dans une liste #
#----------------------------------------------#

def liste():
        fruits=["pomme", "cerise", "orange"]
        fruits.append("melon")
        return fruits

print(liste())
print(liste().append("Melon"))

#integrer le .append() dans la fonction
#de man_re à ce qu'il soit pris en compte dans la demande d'impression
