
#----------------------------------------------#
        # JOB 8 :  #
#----------------------------------------------#

def quoi_manger(type, saison):
        if type =="fruits" and saison=="hiver":
                print("orange, mandarine, kiwi")
        if type =="fruits" and saison=="été":
                print("poire, fraise, cassis")
        if type =="légumes" and saison=="été":
                print("artichaut, auberrgine, navet")
        if type =="légumes" and saison=="hiver":
                print("carotte, topinambour, endive")

quoi_manger("fruits", "hiver")
quoi_manger("fruits", "été")
quoi_manger("légumes", "hiver")
quoi_manger("légumes", "été")
