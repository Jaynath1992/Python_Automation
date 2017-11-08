# 10)	WAP to accept three inputs from the user and find the greatest
# number among 3 numbers. (Get three numbers from raw_input)

def Find_Greatest_Number(num1,num2,num3):
    if num1 > num2 and num1 > num3 :
        print('Greatest number is = %d'%(num1))
    elif num2 > num3 and num2 > num1 :
        print('Greatest number is = %d'%(num2))
    else:
        print('Greatest number is = %d'%(num3))



#Making call to above function

num1 = int(raw_input('Enter first number : '))
num2 = int(raw_input('Enter second number : '))
num3 = int(raw_input('Enter third number : '))

Find_Greatest_Number(num1,num2,num3)
