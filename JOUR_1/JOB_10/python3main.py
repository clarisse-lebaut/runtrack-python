
#----------------------------------------------#
# JOB 10 :SIMULATION FINANCIERE D'INVESTISSMENT #
#----------------------------------------------#

#création de deux variables
#la 1ére pour le montant intial inviesti par l'investisseur
montant_initial_investissement=500
print(f"Montant initial de l'investissement : {montant_initial_investissement}euros.")
#la deuxieme pour le taux de rendement annuel = ici on se dit 5% sur une année = 10% par an
taux_de_rendement_annuel=(100*10/100) 
print(f"Taux de rendement annuel : {taux_de_rendement_annuel}%")

#imrpimer dans le terminal le gain annuel en fonction du rendement
#faire le calcul d'un investissement sur une année

""" le gain annuel correpsond à l'opération 50*500/100 
(50 étant le résulat des 10% frusctifié avec les 500e)
ce qui sur une année avec uun investissement de 500euros on gagne 50euros"""

gain_annuel=montant_initial_investissement*taux_de_rendement_annuel/100
print(f"Gain annuel grâce à l'investissement : {gain_annuel}euros")

#caluler le gain total sur la fin de l'année
gain_total_annuel=gain_annuel+montant_initial_investissement
print(f"Solde après rendement : {gain_total_annuel}")

#inverstisseur augmente son capital de 5000
#ajouter 5000 au capital au taux final sur l'année
ajout_au_capital=5000
nouveau_solde=gain_total_annuel + ajout_au_capital
print(f"Nouveau solde d'investisemment: {nouveau_solde}")

#caluler le nouveau gain de l'investisseur
#affichez le nouveau résultat dans le terminal
nouveau_gain=nouveau_solde*gain_annuel
print(f"Gain après nouvel investissment grâce au rendement : {nouveau_gain}")

#retirer 10% au montal total


#le rendement diminue de 1%


#calculer le montant final des gains


#afficher le résultat final dans le terminal
