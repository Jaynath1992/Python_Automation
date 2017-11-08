import sys

#values = raw_input('Enter two numbers and operation to perform on these numbers : ')

num1 = sys.argv[1]
num2 = sys.argv[2]
operation = sys.argv[3]

if len(sys.argv)<4:
    print('Number of arguments passed should be atleast 3')
    sys.exit(1)
if not (sys.argv[1].isdigit() and sys.argv[2].isdigit()):
    print('Enter digit values only')
    sys.exit(1)

if not (operation.lower() == 'add' or operation.lower() == 'sub' or operation.lower() == 'multiply' or operation.lower() == 'divide'):
    print('Entered operation {0} is not listed:'.format(operation))
    sys.exit(1)
    
    

    
if operation == 'add':
    print('Sum of num1 {0} and num2 {1} is = {2}'.format(num1,num2,int(num1)+ int(num2)))
elif operation == 'sub':
    print('Sub of num1 {0} and num2 {1} is = {2}'.format(num1,num2,int(num1)- int(num2)))
elif operation == 'multiply':
    print('Multiply of num1 {0} and num2 {1} is = {2}'.format(num1,num2,int(num1)* int(num2)))
elif operation == 'divide':
    print('Division of num1 {0} and num2 {1} is = {2}'.format(num1,num2,int(num1)/int(num2)))
else:
    print('operation does not match any of the condition')
    sys.exit(1)
    
    
    

  
