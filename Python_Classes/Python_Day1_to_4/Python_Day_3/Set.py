Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> employees = {(1,2,3):[1,2,3]}
>>> employees
{(1, 2, 3): [1, 2, 3]}
>>> employee = ('Jatin',)
>>> employee[0]
'Jatin'
>>> employee = ('Jatin')
>>> employee[0]
'J'
>>> employee = (['jatin','35'],['Rahul',25])
>>> employee[0][0]= 'rahul'
>>> employee
(['rahul', '35'], ['Rahul', 25])
>>> managers = set(['Akash','Rahul','Bob'])
>>> engineers = set(['Rahul','Vijay'])
>>> managers & engineers
set(['Rahul'])
>>> managers | engineers
set(['Bob', 'Vijay', 'Akash', 'Rahul'])
>>> managers - engineers
set(['Bob', 'Akash'])
>>> 
