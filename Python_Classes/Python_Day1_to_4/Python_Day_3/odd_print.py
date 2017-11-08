number = input('Enter a number:')
count =0
if number < 0:
    print 'Negative numbers..cannot be printed odd numbers'
else:
    while count < 10:
        if number % 2 == 1:
            print 'Odd number %d' %(number)
            count = count + 1
        number = number +1
            
