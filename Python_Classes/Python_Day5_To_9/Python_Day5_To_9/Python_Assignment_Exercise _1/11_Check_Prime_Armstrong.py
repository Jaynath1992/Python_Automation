# 11)	WAP to check whether the user input number is Prime, Armstrong number and
# find out the ascii value of that number.

def Check_Number(num):
    count=0
    for i in range(1,num+1):
        if num % i == 0:
            count=count+1
    if count==2:
        print '%d is prime'%(num)
    else:
        print '%d is not prime'%(num)
    # Armstrong number :  sum of cube of it's digit equal to original number
    sum_val = 0
    orig_num = num
    while(orig_num>0):
        x = orig_num % 10
        sum_val = sum_val + x**3
        orig_num = orig_num / 10
    
    if num == sum_val:
        print '%d is armstrong number'%(num)
    else:
        print '%d is not armstrong number'%(num)


# Making call to above function

number = int(raw_input('Enter Number: '))
Check_Number(number)
        
