# 9)	WAP to find the first hundred prime numbers.

def Get_Prime_Range(n):
    for i in range(1,n):
        count = 0
        for j in range(1,i+1):
            if i % j == 0:
                count = count + 1
        if count == 2:
            print(i)
            



# Making caal to above function
range_val = input('Enter range to find prime numbers:')
Get_Prime_Range(range_val)
