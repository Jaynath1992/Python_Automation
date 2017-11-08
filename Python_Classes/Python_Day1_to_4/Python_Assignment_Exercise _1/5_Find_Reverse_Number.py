# WAP to reverse a given number.

def Reverse_Number():
    num = input('Enter a number to be reversed :')
    original_num = num
    rev = 0
    while(num > 0):
        rem = num % 10
        rev = rev * 10 + rem
        num = num / 10
    else:
        print('Reverse of number %d is = %d'%(original_num,rev))


# Making call to above function

Reverse_Number()
        
