
#----------------------------------------------#
        # JOB 8 : compter les nb pairs #
#----------------------------------------------#

L=[8, 24, 27, 48, 2,16, 9, 7, 84, 91]

#calculer les nombres pairs
somme_des_nombres_pairs = 0
#on initialise un compteur à partir de 0
for i in L:
#dans l'index de la Liste L
        if i%2 ==0:
        #si le nombres que l'index trouve sont divisible par 2 (car un nombre pair est divisible par 2)
                somme_des_nombres_pairs = somme_des_nombres_pairs + i
                #la somme des nombres pairs = sommes des nombres + i pour que l'index cherche tous les nombres pairs
print(f"Le total des nombres pairs est de : {somme_des_nombres_pairs}")
#imprime la somme des nombres pairs





#------- Cheminement pour comprendre comment ça marche
#la somme total de des nombres
somme_total = 0
for i in L:
        somme_total = somme_total + i
print(f"La somme total de cette liste est de : {somme_total}")
#trouver les nombres de chiffres pairs
compteur_de_nombres_pairs = 0
for i in L:
        if i%2 ==0:
                compteur_de_nombres_pairs = compteur_de_nombres_pairs+1
print(f"Il y a : {compteur_de_nombres_pairs} nombres pairs")