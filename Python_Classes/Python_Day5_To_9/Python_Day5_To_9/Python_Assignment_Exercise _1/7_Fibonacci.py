# 7)WAP to create a Fibonacci series of n numbers

def Generate_Fibonacci(n):
    # Initialise variables
    a = 0
    b = 1
    print(a)
    print(b)
    
    for i in range(n-2):
        c = a + b
        print(c)
        a = b
        b = c


# Making call to above function

num  = input('Enter how many fibonaccy numbers : ')

Generate_Fibonacci(num)
