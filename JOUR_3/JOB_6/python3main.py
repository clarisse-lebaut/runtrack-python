
#----------------------------------------------#
        # JOB 6 : POSITIF OU NEGATIF #
#----------------------------------------------#

def comparateur(nombre):
    if nombre < 0:
        return "négatif"
    if nombre > 0:
        return "positif"
    
print(comparateur(-1))
print(comparateur(3))
print(comparateur(9))
print(comparateur(-56))
print(comparateur(0))
print(comparateur(-6))