
#----------------------------------------------#
        # JOB 5 : ALPHABET A L'ENVERS #
#----------------------------------------------#

#définir la valeur de la variable, ici 'alphabet'
alphabet='abcdefghijklmnopqrstuvwxyz'

#commande pour print en reverse
#première méthode de retournement
#c'est ce qu'on appel une boucle avec for
reversed_alphabet=" "
for letter in alphabet:
    reversed_alphabet = letter + reversed_alphabet
print(reversed_alphabet)

""" 
Ce qui se passe dans la ligne de commande juste au dessus :

- tu définis une varaiblee (ici = alaphabet = 'abcedfghijklmnopqrstuvwxyz')
- definir la variable revesed_alphabet (je sais pas encore pourquoi je dois mettre les guillemets de la sorte)
- puis for letter in alphabet veut dire pour les lettre dans la variable nommée
- faire appel au revers_nomvariable est égale à la lettre + le parametre indiqué
- impression dans le terminal 
"""

#deuxième méthode de retournement
print(alphabet[-1:1]) 
print(alphabet[::-1])
"""faire attention à la manière dont on place les chiffres entre les accolades"""