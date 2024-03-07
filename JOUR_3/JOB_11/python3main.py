
#----------------------------------------------#
        # JOB 11 : HEURE ET MINUTES #
#----------------------------------------------#

def time_to_text(nbr_entier, affiche_en_console):
        heure = nbr_entier//60
        minute_restante = nbr_entier %60
        affiche_en_console = f"{heure} heures et {minute_restante} minutes."
        print(affiche_en_console)

time_to_text(160,"")
time_to_text(120,"")
time_to_text(90,"")
time_to_text(60,"")
time_to_text(30,"")
time_to_text(215,"")
time_to_text(72,"")

"""
Résumé :

on divise le nombe entier //60
puis on redivise le nombre entier avec cette fois-cit un modulo pour avoir le reste
il nous faut donc d'une part le quotient du nombre eniter puis d'autre part le reste du nombres entier =
cela nous permet d'avoir la conversion en heures et minutes d'un nombre entier

concernant le affiche_console, utlisation des doubles comas pour remplir cette fonction et permettre l'impression
en console

"""