# WAP to convert temperature from degree centigrade to
# Fahrenheit. Ex: (°C × 9/5) + 32 = °F

def Centigrade_To_Farenhite_Conversion():
    centigrade = input('Enter temprature in centigrade : ')
    farenhite = (9 * centigrade)/5 + 32
    print('Centigrade := %r C converiosn to farenhite is : = %r F'%(centigrade,farenhite))

# Making a call to above function

Centigrade_To_Farenhite_Conversion()

