Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list1 = [1,5,2,10,11,20,12]
>>> type(list1)
<type 'list'>
>>> dir(list1)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(sorted)
Help on built-in function sorted in module __builtin__:

sorted(...)
    sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list

>>> list1.sort()
>>> list1
[1, 2, 5, 10, 11, 12, 20]
>>> list1.sort(reverse=True)
>>> list1
[20, 12, 11, 10, 5, 2, 1]
>>> list1 = ['aakash','Amit','Aakash','ameet']
>>> list1.sort()
>>> list1
['Aakash', 'Amit', 'aakash', 'ameet']
>>> # python sort the list based on ascii value
>>> asc('a')

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    asc('a')
NameError: name 'asc' is not defined
>>> ord('a')
97
>>> # Key - holds function (it can be udf or lambda function)
>>> list1.sort(key=str.upper())

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list1.sort(key=str.upper())
TypeError: descriptor 'upper' of 'str' object needs an argument
>>> list1.sort(key=str.upper)
>>> list1
['Aakash', 'aakash', 'ameet', 'Amit']
>>> list1 = [['Jatin',35],['Mahesh',23],['Rajesh',45],['Neha',31]]
>>> list1.sort(key=lambda x: x[1])
>>> list1
[['Mahesh', 23], ['Neha', 31], ['Jatin', 35], ['Rajesh', 45]]
>>> list1.sort(key=lambda x: x[1],reverse=True)
>>> list1
[['Rajesh', 45], ['Jatin', 35], ['Neha', 31], ['Mahesh', 23]]
>>> help(sorted())

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    help(sorted())
TypeError: Required argument 'iterable' (pos 1) not found
>>> help(sorted)
Help on built-in function sorted in module __builtin__:

sorted(...)
    sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list

>>> list1 = [10,4,15,12,20]
>>> sorted(list1)
[4, 10, 12, 15, 20]
>>> list1
[10, 4, 15, 12, 20]
>>> sorted(list1,reverse=True)
[20, 15, 12, 10, 4]
>>> employee = [['Jaynath',35],['Mahesh',25],['Rajesh',30],['Niharika',20]]
>>> sorted(employee,key=lambda x: x[1])
[['Niharika', 20], ['Mahesh', 25], ['Rajesh', 30], ['Jaynath', 35]]
>>> # The only difference between sorted and sort is that, sorted returns a new list it dows not modify the original list, but in case of sort function it modify the original list, it dows not returns any new list
>>> help(sorted)
Help on built-in function sorted in module __builtin__:

sorted(...)
    sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list

>>> # Iterable object which can be iterate over, it can be list,dictionary,tuple,string
>>> employee = {'Jaynath':30000,'Rajesh':42000,'Neha':45000}
>>> dir(employee)
['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
>>> sorted(employee,key=lambda x:x[1])
['Jaynath', 'Rajesh', 'Neha']
>>> sorted(employee,key=lambda x: x[0][1])

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    sorted(employee,key=lambda x: x[0][1])
  File "<pyshell#37>", line 1, in <lambda>
    sorted(employee,key=lambda x: x[0][1])
IndexError: string index out of range
>>> employee.items
<built-in method items of dict object at 0x0399BF60>
>>> employee.items()
[('Neha', 45000), ('Jaynath', 30000), ('Rajesh', 42000)]
>>> sorted(employee,key=lambda x: x[0][1])

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    sorted(employee,key=lambda x: x[0][1])
  File "<pyshell#40>", line 1, in <lambda>
    sorted(employee,key=lambda x: x[0][1])
IndexError: string index out of range
>>> sorted(employee.items(),key=lambda x: x[0][1])
[('Jaynath', 30000), ('Rajesh', 42000), ('Neha', 45000)]
>>> sorted(employee.items(),key=lambda x: x[0][1],reverse=True)[0][1]
45000
>>> sorted(employee.items(),key=lambda x: x[0][1],reverse=True)[0][0]
'Neha'
>>> sorted(employee.items(),key=lambda x: x[1])
[('Jaynath', 30000), ('Rajesh', 42000), ('Neha', 45000)]
>>> sorted(employee.items(),key=lambda x: x[1])[0][0]
'Jaynath'
>>> sorted(employee.items(),key=lambda x: x[1],reverse=True)[:2]
[('Neha', 45000), ('Rajesh', 42000)]
>>> employee = {1:['Jatin','IT',30000],2:['Rahul','HR',20000],3:['Neha','Admin',15000],4:['raj','IT',56000]}
>>> employee.items()
[(1, ['Jatin', 'IT', 30000]), (2, ['Rahul', 'HR', 20000]), (3, ['Neha', 'Admin', 15000]), (4, ['raj', 'IT', 56000])]
>>> #find max salry employee in IT dept
>>> sorted(employee.items,key=lambda x:x[1][2] if x[1][1]=='IT',reverse=True)[1][0]
SyntaxError: invalid syntax
>>> sorted(employee.items,key=lambda x:x[1][2] if x[1][1]=='IT' else 0,reverse=True)[1][0]

Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    sorted(employee.items,key=lambda x:x[1][2] if x[1][1]=='IT' else 0,reverse=True)[1][0]
TypeError: 'builtin_function_or_method' object is not iterable
>>> sorted(employee.items,key=lambda x:x[1][2] if x[1][2]=='IT' else 0,reverse=True)[1][0]

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    sorted(employee.items,key=lambda x:x[1][2] if x[1][2]=='IT' else 0,reverse=True)[1][0]
TypeError: 'builtin_function_or_method' object is not iterable
>>> sorted(employee.items,key=lambda x:x[1][2] if x[1][1]=='IT' else 0,reverse=True)[1][0]

Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    sorted(employee.items,key=lambda x:x[1][2] if x[1][1]=='IT' else 0,reverse=True)[1][0]
TypeError: 'builtin_function_or_method' object is not iterable
>>> sorted(employee.items,key=lambda x:x[1][2] if x[1][1]=='IT' else 0,reverse=True)

Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    sorted(employee.items,key=lambda x:x[1][2] if x[1][1]=='IT' else 0,reverse=True)
TypeError: 'builtin_function_or_method' object is not iterable
>>> sorted(employee.items(),key=lambda x:x[1][2] if x[1][1]=='IT' else 0,reverse=True)
[(4, ['raj', 'IT', 56000]), (1, ['Jatin', 'IT', 30000]), (2, ['Rahul', 'HR', 20000]), (3, ['Neha', 'Admin', 15000])]
>>> sorted(employee.items(),key=lambda x:x[1][2] if x[1][1]=='IT' else 0,reverse=True)[1][0]
1
>>> sorted(employee.items(),key=lambda x:x[1][2] if x[1][1]=='IT' else 0,reverse=True)[1][0]
1
>>> sorted(employee.items(),key=lambda x:x[1][2] if x[1][1]=='IT' else 0,reverse=True)[0][1][0]
'raj'
>>> 
