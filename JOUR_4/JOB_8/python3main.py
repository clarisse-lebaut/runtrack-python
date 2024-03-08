
#----------------------------------------------#
        # JOB 8 : compter les nb pairs #
#----------------------------------------------#

#définir la liste
L=[8, 24, 17, 48, 2, 16, 9, 7, 84, 91]
print(L)
#trouver tous les nombres pairs de cette liste
for index in L:
        if index%2 ==0:
                print(f"{index} est un nombre pairs")
#trouver combien il y a de chiffre pairs au total dans cette liste
for index in L:
        if index == index%10:
                print(f" Il y a {index} nombres pairs")

#calculer tous les nombres pairs entre eux
#il faut trouver comment récupérer les nombres divisble par 2 (=ce sont les nb pairs)
somme = index%2 + index 
print(f"{somme} est la somme total des nombres pairs de cette liste")


#somme total à trouver de nombres pairs de cette liste
print(8+24+48+2+16+84)