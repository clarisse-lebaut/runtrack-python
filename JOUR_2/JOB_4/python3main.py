
#----------------------------------------------#
    # JOB 4 : TABLES DE MULTIPLICATIONS #
#----------------------------------------------#

#crée un programme qui affiche dans le terminal les tables de mutliplications de 1 à N
#N est un entier saisie par l'utilisateur --> le rempalcer par une autre variable

#permettre la saisie par l'utilisateur
table_voulu=input("Quel table de mutliplciation veux-tu ? ")
table_voulu=int(table_voulu) 

#boucle qui permet de générer les tables de mutiplication
multiplier_par= range(11)
for multiplier_par in range(11):
    if table_voulu >0:
        print(f"{table_voulu} x {multiplier_par} = {table_voulu * multiplier_par}")




