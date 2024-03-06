
#----------------------------------------------#
    # POUR ALLER PLUS LOIN : triangles #
#----------------------------------------------#

#permettre la saisir de l'utilistateur
longeur_une = int(input("Longueur a : "))
longeur_deux = int(input("Longueur b : "))
longeur_trois = int(input("Longueur c : "))

print(" ____________ ")

#variable appelable pour chacune des longeurs choisis par l'utilisateur
a=longeur_une
b=longeur_deux
c=longeur_trois

#défnir la def d'un triangle dans une variable pour n'avoir qu'a l'appeler dans la suite du programme



#est-il possible de construire un triangle ?
if a+b+c ==6: #cette condition doit dire <si les 3 côtés peuvent être fermé>
    print("on peut constuire un triangle :")
    #ici on a une ébauche de condition à retravailler, ne sont pas correctes
    if a*a+b*b==c*c: #formule pour déterminer la forme
        #si 2 côtés égaux ET 2 angles égaux ET un angle à 90°
        print("RECTANGLE ISOCELE")
    if a*a+b*b==c*c: #formule pour déterminer la forme
        #si 3 côtés forment un angle a 90°
        print("RECTANGLE")
    if (a==b or a==c) or (b==c or b==a) or (c==a or c==b): #formule pour déterminer la forme 
        #si 2 côtés sont égaux ET que 2 angles sont égaux
        print("ISOCELE")
    if a == b == c: #formule pour déterminer la forme
        #si 3 côtés sont égaux ET que 3 angles sont égaux
        print("EQUILATERAL")
    else:
        print("quelconque")
else:
    print("ont peut pas constuire un triangle")