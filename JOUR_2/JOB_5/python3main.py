
#----------------------------------------------#
    # JOB 5  : FIZZ, BUZZ ET FIZZBUZZZ #
#----------------------------------------------#

#le modulo = a%b==0 --> permet de faire certains calculs
#dans ce code : permet de vérifier les multiples

""" [t(=variable) for t(=varaible) in range(101) if t%3==0] --> exemple de modulo """

for nombres_entier in range(1, 101):
    if nombres_entier%3 ==0 and nombres_entier%5 ==0: 
    #--> mettre le and dans le if tout en hait si il y a plusieurs conditions !
        print("FizzBuzz")
    elif nombres_entier%3 ==0:
        print("Fizz")
    elif nombres_entier%5 ==0:
        print("Buzz")
    else:
        print(nombres_entier)
    
