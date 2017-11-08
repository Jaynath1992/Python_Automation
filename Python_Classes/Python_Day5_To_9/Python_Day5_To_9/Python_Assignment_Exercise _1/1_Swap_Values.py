# Program to swap values of two variable without using third variable

def Swap_Values(a,b):
    print('Before Swap value of a := %d and b := %d' %(a,b))
    a = a + b
    b = a - b
    a = a - b
    print('After Swaping value of a = %d and b = %d ' %(a,b))


# Make a call to above function

Swap_Values(20,20)
    
    
