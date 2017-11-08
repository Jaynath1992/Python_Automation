'''
This is the help page of the module
'''

def add(a, b):
    '''
    This is an function which accept a and b and return a + b
    add(a, b) -> a + b (Interger)
    '''
    return a + b

def mul(a, b):
    '''
    This is an function which accept a and b and return a * b
    mul(a, b) -> a * b (Interger)
    '''
    return a * b

def sub(a, b):
    '''
    This is an function which accept a and b and return a * b
    mul(a, b) -> a * b (Interger)
    '''
    return a - b

pi = 3.14
e= 2.7

# Standard boiler plate in python

if __name__ == '__main__':
    print 'Addition is :',add(10,20)
    print 'Multiplication is :',mul(10,20)
