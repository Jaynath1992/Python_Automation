# 8)	WAP to get the factorial of user defined number.

def Calculate_Factorial(num):
    fact = 1
    for i in range(num,1,-1):
        fact = fact * i
    print('Factorial of number %d = %d'%(num,fact))



# making call to above function

num = input('Enter number to get it\'s factorial : ')
Calculate_Factorial(num)
