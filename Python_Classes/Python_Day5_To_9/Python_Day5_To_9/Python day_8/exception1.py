import sys
try:
    number  = input('Enter the  number: ')
    print 'Division of number {0} by {1} is : {2}'.format(100,number,100/number)
    print number + 'Jatin'
except ZeroDivisionError:
    try:
        number = input('Please do not provide 0, Enter the number again: ')
        print ' Division of number {0} by {1} is {2}'.format(100,number,100/number)
    except ZeroDivisionError:
        print 'Bhai rehne do, tumse na ho payega!'
    #raise ValueError('Division of number {0} by {1} is {2}'.format(100,number,100/number))
except NameError:
    print 'Got a name error, existing'

# Generic excepption
except Exception:
    print 'Got an exception'
    print ''
# will execute when try block executed successfully
else:
    print 'Exception Name',sys.exc_info()[0]
    print 'Exception reason',sys.exc_info()[1]

print 'Program completed'