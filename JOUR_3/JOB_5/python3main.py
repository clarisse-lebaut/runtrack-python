
#----------------------------------------------#
        # JOB 5 : FONCTION ET CALCUL #
#----------------------------------------------#

def calcule(num1, operator, num2):
        if operator == '+':
                return num1+num2
        if operator == '-':
                return num1-num2
        if operator == '*':
                return num1*num2
        if operator == '/':
                return num1/num2
        if operator == '%':
                return num1%num2
        return num1, operator, num2

print(calcule(2, '+', 6))
print(calcule(2, '-', 6))
print(calcule(2, '*', 6))
print(calcule(2, '/', 6))
print(calcule(2, '%', 6))