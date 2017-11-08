# 14) WAP to find out the leap year.
# (Except a year from the user using raw_input)


# A leap year is exactly divisible by 4 except for century years
# (years ending with 00). The century year is a leap year only if
# it is perfectly divisible by 400. For example

def Check_LeapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print 'Year is leap year : ' + str(year)
    else:
        print 'Year is not leap year : ' + str(year)
        

# Call to above function

year = int(raw_input('Enter year to be checked: '))
Check_LeapYear(year)
