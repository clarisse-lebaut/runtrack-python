
#----------------------------------------------#
                # JOB 9 : MOYENNE #
#----------------------------------------------#

nb1=int(input("Saisir note 1 : "))
nb2=int(input("Saisir note 2 : "))
nb3=int(input("Saisir note 3 : "))

def moyenne():
        calcul = nb1 + nb2 + nb3
        moyenne_etudiant = calcul //3 
        print(f"Moyenne de l'étudiant : {moyenne_etudiant}")
        if moyenne_etudiant <=7:
                print ("Commentaire : Eleve devant faire des effort")
        if moyenne_etudiant >=8 and moyenne_etudiant <=10:
                print ("Commentaire : Eleve moyen")
        if moyenne_etudiant >=11 and moyenne_etudiant <=14:
                print ("Commentaire : Bon élève")
        if moyenne_etudiant >=15 and moyenne_etudiant <=20:
                print ("Commentaire : Très bon élève") 

moyenne() #pour appeler la fonction, simplement écrire ce qu'il y a d'écrit après def, pas plus 
