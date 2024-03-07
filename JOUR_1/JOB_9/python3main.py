
#----------------------------------------------#
        # JOB 9 : GESTION D'INVENTAIRE #
#----------------------------------------------#

#création de variables
nom="vestes"
prix_unitaire=15
quantité_en_stock=200
#affichage formaté en console
print(f"Nous vendons des {nom}, à {prix_unitaire} euros l'unité. Il en reste {quantité_en_stock} en stock.")
print("Quantité diponible: ", quantité_en_stock)

#ajout d'articles dans les stocks
nouvelle_quantité=quantité_en_stock + 50
print(f"Nous avons augmenter nos stocks. Nous avons mainteant {nouvelle_quantité} vestes.")

#demande d'articles voulu
quantité_voulu = input("Nombres d'articles voulu : ")
quantité_voulu=int(quantité_voulu) 
# souviens toi que le int concerne les nb entiers

#calcul de la différence entre quantité restante et quantité voulu
quantité_restante = nouvelle_quantité - quantité_voulu
#mise a jour du stock imprimer, on récupère la valeur du input
print("Mise à jour du stock : ", quantité_restante) 

#augmentation de produit
#calculer la remise en pourcentage : nb total = (nb du pourcentage a calculer x 100) / par nle nb total
#calculer une augmentation en pourcentage : (prix de l'article de base x 10 / 100)
calcul=(prix_unitaire*10/100)
print(f"Augmentation de {calcul} euros.")

nouveau_prix= calcul + prix_unitaire
print(f"Nous connaissont une inflation de 10% sur l'ensemble de nos articles. \n Les {nom} valent mainteannt {nouveau_prix}.")