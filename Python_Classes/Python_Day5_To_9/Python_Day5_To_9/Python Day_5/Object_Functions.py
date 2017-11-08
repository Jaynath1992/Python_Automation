Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a='jaynath'
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> name = 'jatin'
>>> name.count('at')
1
>>> help(name.center)
Help on built-in function center:

center(...)
    S.center(width[, fillchar]) -> string
    
    Return S centered in a string of length width. Padding is
    done using the specified fill character (default is a space)

>>> name.center(200)
'                                                                                                 jatin                                                                                                  '
>>> name.center()

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    name.center()
TypeError: center() takes at least 1 argument (0 given)
>>> name.center
<built-in method center of str object at 0x03487E20>
>>> name.center(400)
'                                                                                                                                                                                                     jatin                                                                                                                                                                                                      '
>>> name.center(300)
'                                                                                                                                                   jatin                                                                                                                                                    '
>>> help(name.count)
Help on built-in function count:

count(...)
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are interpreted
    as in slice notation.

>>> name.count()

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    name.count()
TypeError: count() takes at least 1 argument (0 given)
>>> count(name)

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count(name)
NameError: name 'count' is not defined
>>> name.count()

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    name.count()
TypeError: count() takes at least 1 argument (0 given)
>>> name.count('jatin')
1
>>> help(name.center)
Help on built-in function center:

center(...)
    S.center(width[, fillchar]) -> string
    
    Return S centered in a string of length width. Padding is
    done using the specified fill character (default is a space)

>>> account='1101'
>>> account.center(16,'X')
'XXXXXX1101XXXXXX'
>>> account.encode('base64')
'MTEwMQ==\n'
>>> encryptedAccount = account.encode('base64')
>>> print encryptedAccount
MTEwMQ==

>>> encryptedAccount.decode('base64')
'1101'
>>> password = 'March@Apple2017'
>>> encryptedPassword = password.encode('base64')
>>> print encryptedPassword
TWFyY2hAQXBwbGUyMDE3

>>> decryptedPasswword = encryptedPassword.decode('base64')
>>> print decryptedPassword

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print decryptedPassword
NameError: name 'decryptedPassword' is not defined
>>> print decryptedPasswword
March@Apple2017
>>> filename = 'file.txt'
>>> filename.endsWith('.txt')

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    filename.endsWith('.txt')
AttributeError: 'str' object has no attribute 'endsWith'
>>> filename.endswith('.txt')
True
>>> filename.startswith('file')
True
>>> filename.find('i')
1
>>> filename.find('z')
-1
>>> help(''.find)
Help on built-in function find:

find(...)
    S.find(sub [,start [,end]]) -> int
    
    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Return -1 on failure.

>>> help(''.format)
Help on built-in function format:

format(...)
    S.format(*args, **kwargs) -> string
    
    Return a formatted version of S, using substitutions from args and kwargs.
    The substitutions are identified by braces ('{' and '}').

>>> 'Hello {0},Please pay me rupees {1}'.format('jaynath',10)
'Hello jaynath,Please pay me rupees 10'
>>> 'Hello {name}, Please pay me dollar {dollar}'.format(name='jaynath',dollar=10)
'Hello jaynath, Please pay me dollar 10'
>>> 'Hello {name}, Please pay me dollar {dollar}'.format(name='jaynath',dollr=10)

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    'Hello {name}, Please pay me dollar {dollar}'.format(name='jaynath',dollr=10)
KeyError: 'dollar'
>>> 'Hello {name}, Please pay me dollar {dollar}'.format(dollar=10,name='jaynath')
'Hello jaynath, Please pay me dollar 10'
>>> 'Hello {1},please find ur marks in math={1},physics={2} and chemistry={3}'.format('jaynath',80,90,45)
'Hello 80,please find ur marks in math=80,physics=90 and chemistry=45'
>>> 
>>> 'Hello {0},please find ur marks in math={1},physics={2} and chemistry={3}'.format('jaynath',80,90,45)
'Hello jaynath,please find ur marks in math=80,physics=90 and chemistry=45'
>>> ''.join(map(lambda x: str(x),range(10)))
'0123456789'
>>> allwords=filename.split('.')
>>> allwords
['file', 'txt']
>>> '.'.join(allwords)
'file.txt'
>>> map(lambda x: str(x),range(10))
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> ''.join(map(lambda x: str(x),range(10)))
'0123456789'
>>> help(''.ljust)
Help on built-in function ljust:

ljust(...)
    S.ljust(width[, fillchar]) -> string
    
    Return S left-justified in a string of length width. Padding is
    done using the specified fill character (default is a space).

>>> '1234'.ljust(16,'X')
'1234XXXXXXXXXXXX'
>>> '1234'.rjust(16,'X')
'XXXXXXXXXXXX1234'
>>> account='873823947993'
>>> account[-4:].rjust(16,'X')
'XXXXXXXXXXXX7993'
>>> name = '     ja t i n   '
>>> name.replace(' ','')
'jatin'
>>> name='jatin\n\n\r'
>>> name.strip()
'jatin'
>>> name.replace('\n','r',5)
'jatinrr\r'
>>> name.replace('\n','r',1)
'jatinr\n\r'
>>> names=['Ashish','Ajay','Amit','Vivek']
>>> dir(names)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(names.append)
Help on built-in function append:

append(...)
    L.append(object) -- append object to end

>>> names.append('Mohan')
>>> names
['Ashish', 'Ajay', 'Amit', 'Vivek', 'Mohan']
>>> help(names.count)
Help on built-in function count:

count(...)
    L.count(value) -> integer -- return number of occurrences of value

>>> names.append('Ajay')
>>> names.count()

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    names.count()
TypeError: count() takes exactly one argument (0 given)
>>> names.count('Ajay')
2
>>> help(names.extend)
Help on built-in function extend:

extend(...)
    L.extend(iterable) -- extend list by appending elements from the iterable

>>> names.append('['Raj','Neha']')
SyntaxError: invalid syntax
>>> names.append(['Raj','Neha'])
>>> names
['Ashish', 'Ajay', 'Amit', 'Vivek', 'Mohan', 'Ajay', ['Raj', 'Neha']]
>>> names.extend(['Sneha','Smruti','Rekha'])
>>> names
['Ashish', 'Ajay', 'Amit', 'Vivek', 'Mohan', 'Ajay', ['Raj', 'Neha'], 'Sneha', 'Smruti', 'Rekha']
>>> names.index('Ajay')
1
>>> names.index('Smruti')
8
>>> names.insert(4,'Jaynath')
>>> names
['Ashish', 'Ajay', 'Amit', 'Vivek', 'Jaynath', 'Mohan', 'Ajay', ['Raj', 'Neha'], 'Sneha', 'Smruti', 'Rekha']
>>> help(names.insert)
Help on built-in function insert:

insert(...)
    L.insert(index, object) -- insert object before index

>>> help(names.pop)
Help on built-in function pop:

pop(...)
    L.pop([index]) -> item -- remove and return item at index (default last).
    Raises IndexError if list is empty or index is out of range.

>>> names.pop(4)
'Jaynath'
>>> names
['Ashish', 'Ajay', 'Amit', 'Vivek', 'Mohan', 'Ajay', ['Raj', 'Neha'], 'Sneha', 'Smruti', 'Rekha']
>>> help(names.remove)
Help on built-in function remove:

remove(...)
    L.remove(value) -- remove first occurrence of value.
    Raises ValueError if the value is not present.

>>> names.remove('Rekha')
>>> names
['Ashish', 'Ajay', 'Amit', 'Vivek', 'Mohan', 'Ajay', ['Raj', 'Neha'], 'Sneha', 'Smruti']
>>> help(reverse)

Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    help(reverse)
NameError: name 'reverse' is not defined
>>> help(names.reverse)
Help on built-in function reverse:

reverse(...)
    L.reverse() -- reverse *IN PLACE*

>>> names.reverse()
>>> names
['Smruti', 'Sneha', ['Raj', 'Neha'], 'Ajay', 'Mohan', 'Vivek', 'Amit', 'Ajay', 'Ashish']
>>> l='raj'
>>> l.reverse()

Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    l.reverse()
AttributeError: 'str' object has no attribute 'reverse'
>>> help(names.sort)
Help on built-in function sort:

sort(...)
    L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
    cmp(x, y) -> -1, 0, 1

>>> names.sort()
>>> names
[['Raj', 'Neha'], 'Ajay', 'Ajay', 'Amit', 'Ashish', 'Mohan', 'Smruti', 'Sneha', 'Vivek']
>>> names
[['Raj', 'Neha'], 'Ajay', 'Ajay', 'Amit', 'Ashish', 'Mohan', 'Smruti', 'Sneha', 'Vivek']
>>> names.extend({'salary':40000})
>>> names
[['Raj', 'Neha'], 'Ajay', 'Ajay', 'Amit', 'Ashish', 'Mohan', 'Smruti', 'Sneha', 'Vivek', 'salary']
>>> names.sort('Sneha')

Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    names.sort('Sneha')
TypeError: 'str' object is not callable
>>> names.sort(key=Ajay)

Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    names.sort(key=Ajay)
NameError: name 'Ajay' is not defined
>>> names.sort()
>>> names
[['Raj', 'Neha'], 'Ajay', 'Ajay', 'Amit', 'Ashish', 'Mohan', 'Smruti', 'Sneha', 'Vivek', 'salary']
>>> names.pop(0)
['Raj', 'Neha']
>>> names
['Ajay', 'Ajay', 'Amit', 'Ashish', 'Mohan', 'Smruti', 'Sneha', 'Vivek', 'salary']
>>> names.remove(0)

Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    names.remove(0)
ValueError: list.remove(x): x not in list
>>> names.remove('Ajay')
>>> names
['Ajay', 'Amit', 'Ashish', 'Mohan', 'Smruti', 'Sneha', 'Vivek', 'salary']
>>> names.sort(key='Ajay')

Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    names.sort(key='Ajay')
TypeError: 'str' object is not callable
>>> names.sort(key=lambda x:names[-1])

Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    names.sort(key=lambda x:names[-1])
  File "<pyshell#108>", line 1, in <lambda>
    names.sort(key=lambda x:names[-1])
IndexError: list index out of range
>>> names.sort(key=lambda name:names[0])

Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    names.sort(key=lambda name:names[0])
  File "<pyshell#109>", line 1, in <lambda>
    names.sort(key=lambda name:names[0])
IndexError: list index out of range
>>> names
['Ajay', 'Amit', 'Ashish', 'Mohan', 'Smruti', 'Sneha', 'Vivek', 'salary']
>>> names.insert(2,'Jaynath')
>>> names
['Ajay', 'Amit', 'Jaynath', 'Ashish', 'Mohan', 'Smruti', 'Sneha', 'Vivek', 'salary']
>>> names.sort()
>>> names
['Ajay', 'Amit', 'Ashish', 'Jaynath', 'Mohan', 'Smruti', 'Sneha', 'Vivek', 'salary']
>>> help(names.reverse)
Help on built-in function reverse:

reverse(...)
    L.reverse() -- reverse *IN PLACE*

>>> names.reverse()
>>> names
['salary', 'Vivek', 'Sneha', 'Smruti', 'Mohan', 'Jaynath', 'Ashish', 'Amit', 'Ajay']
>>> names.reverse()
>>> names
['Ajay', 'Amit', 'Ashish', 'Jaynath', 'Mohan', 'Smruti', 'Sneha', 'Vivek', 'salary']
>>> names.sort()
>>> names
['Ajay', 'Amit', 'Ashish', 'Jaynath', 'Mohan', 'Smruti', 'Sneha', 'Vivek', 'salary']
>>> names.sort(key='J')

Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    names.sort(key='J')
TypeError: 'str' object is not callable
>>> names.extend(['Raj','Shreya','Jadeja'])
>>> names
['Ajay', 'Amit', 'Ashish', 'Jaynath', 'Mohan', 'Smruti', 'Sneha', 'Vivek', 'salary', 'Raj', 'Shreya', 'Jadeja']
>>> names.insert(2,['Vinayak','Sneha','Rahil'])
>>> names
['Ajay', 'Amit', ['Vinayak', 'Sneha', 'Rahil'], 'Ashish', 'Jaynath', 'Mohan', 'Smruti', 'Sneha', 'Vivek', 'salary', 'Raj', 'Shreya', 'Jadeja']
>>> mylist = [["john", 1, "a"], ["larry", 0, "b"]]
>>> mylist.sort(key=lambda mylist : mylist[0][1])
>>> mylist
[['larry', 0, 'b'], ['john', 1, 'a']]
>>> cmp('jay','raj')
-1
>>> cmp('jay','vaibhav')
-1
>>> cmp(12,12)
0
>>> cmp(11,12)
-1
>>> cmp(12,11)
1
>>> employee = [['Jatin,35'],['Akash',24],['Mahesh',28],['Amit',21]]
>>> employee.sort(key=lambda x:x[0][1])
>>> employee
[['Jatin,35'], ['Mahesh', 28], ['Akash', 24], ['Amit', 21]]
>>> employee.sort(key=lambda x:x[1])

Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    employee.sort(key=lambda x:x[1])
  File "<pyshell#138>", line 1, in <lambda>
    employee.sort(key=lambda x:x[1])
IndexError: list index out of range
>>> emmployee

Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    emmployee
NameError: name 'emmployee' is not defined
>>> employee
[['Jatin,35'], ['Mahesh', 28], ['Akash', 24], ['Amit', 21]]
>>> employee.sort(key=lambda x: x[1])

Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    employee.sort(key=lambda x: x[1])
  File "<pyshell#141>", line 1, in <lambda>
    employee.sort(key=lambda x: x[1])
IndexError: list index out of range
>>> employee = [['Jatin',35],['Akash',24],['Mahesh',28],['Amit',21]]
>>> employee.sort((key=lambda x:x[1])
	      
SyntaxError: invalid syntax
>>> employee.sort(key=lambda x:x[1])
>>> employee
[['Amit', 21], ['Akash', 24], ['Mahesh', 28], ['Jatin', 35]]
>>> employee = {'Jatin':30000,'Rahul':20000,'Akash':40000}
>>> # Want to find out name of employee who has maximum salary
>>> 
>>> employee.items
<built-in method items of dict object at 0x03521B70>
>>> employee.items()
[('Jatin', 30000), ('Akash', 40000), ('Rahul', 20000)]
>>> sorted(employee.items(),key=lambda x : x[1],reverse=True)
[('Akash', 40000), ('Jatin', 30000), ('Rahul', 20000)]
>>> sorted(employee.items(),key=lambda x : x[1],reverse=True)[0][0]
'Akash'
>>> sorted(employee.items(),key=lambda x : x[1],reverse=True)[:2]
[('Akash', 40000), ('Jatin', 30000)]
>>> employee = {1:['Jatin','IT',30000],2:['Rahul','HR',20000],3:['Akash','IT',40000],4:['Vijay','IT',60000]}
>>> # want to find name of person having max salary in IT dept
>>> employee.items()
[(1, ['Jatin', 'IT', 30000]), (2, ['Rahul', 'HR', 20000]), (3, ['Akash', 'IT', 40000]), (4, ['Vijay', 'IT', 60000])]
>>> sorted(employee.items(),key=lambda x:x[1][2] if x[1][1]='IT' else 0,reverse=True)[0][1][0]
SyntaxError: invalid syntax
>>>  sorted(employee.items(),key=lambda x:x[1][2] if x[1][1]=='IT' else 0,reverse=True)[0][1][0]
 
  File "<pyshell#167>", line 2
    sorted(employee.items(),key=lambda x:x[1][2] if x[1][1]=='IT' else 0,reverse=True)[0][1][0]
    ^
IndentationError: unexpected indent
>>> sorted(employee.items(),key=lambda x:x[1][2] if x[1][1]=='IT' else 0,reverse=True)[0][1][0]
'Vijay'
>>> employee = {'name':'Jatin','age':42}
>>> dir(employee)
['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
>>> help({}.clear)
Help on built-in function clear:

clear(...)
    D.clear() -> None.  Remove all items from D.

>>> employee.clear()
>>> employee
{}
>>> help({}.copy)
Help on built-in function copy:

copy(...)
    D.copy() -> a shallow copy of D

>>> employee={'name':'Jatin','Age':35,'Salary':30000}
>>> employee.copy()
{'Salary': 30000, 'Age': 35, 'name': 'Jatin'}
>>> employee1=employee.copy()
>>> employee1
{'Salary': 30000, 'Age': 35, 'name': 'Jatin'}
>>> employee
{'Salary': 30000, 'Age': 35, 'name': 'Jatin'}
>>> employee['Location':'Pune']

Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    employee['Location':'Pune']
TypeError: unhashable type
>>> employee['Location']='Pune'
>>> employee
{'Salary': 30000, 'Age': 35, 'name': 'Jatin', 'Location': 'Pune'}
>>> employee1
{'Salary': 30000, 'Age': 35, 'name': 'Jatin'}
>>> help({}.get)
Help on built-in function get:

get(...)
    D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.

>>> employee.get('name')
'Jatin'
>>> help({}.has_key)
Help on built-in function has_key:

has_key(...)
    D.has_key(k) -> True if D has a key k, else False

>>> employee.has_key('name')
True
>>> employee.has_key('loc')
False
>>> help({}.items)
Help on built-in function items:

items(...)
    D.items() -> list of D's (key, value) pairs, as 2-tuples

>>> employee.items()
[('Salary', 30000), ('Age', 35), ('name', 'Jatin'), ('Location', 'Pune')]
>>> help({}.iteritems())
Help on dictionary-itemiterator object:

class dictionary-itemiterator(object)
 |  Methods defined here:
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __iter__(...)
 |      x.__iter__() <==> iter(x)
 |  
 |  __length_hint__(...)
 |      Private method returning an estimate of len(list(it)).
 |  
 |  next(...)
 |      x.next() -> the next value, or raise StopIteration

>>> employee.iteritems()
<dictionary-itemiterator object at 0x035287E0>
>>> print employee
{'Salary': 30000, 'Age': 35, 'name': 'Jatin', 'Location': 'Pune'}
>>> help(keys)

Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    help(keys)
NameError: name 'keys' is not defined
>>> help({}.keys)
Help on built-in function keys:

keys(...)
    D.keys() -> list of D's keys

>>> employee.keys()
['Salary', 'Age', 'name', 'Location']
>>> help({}.pop)
Help on built-in function pop:

pop(...)
    D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
    If key is not found, d is returned if given, otherwise KeyError is raised

>>> employee.pop()

Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    employee.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> employee.pop('salary')

Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    employee.pop('salary')
KeyError: 'salary'
>>> employee.pop('Salary')
30000
>>> employee
{'Age': 35, 'name': 'Jatin', 'Location': 'Pune'}
>>> help({}.values)
Help on built-in function values:

values(...)
    D.values() -> list of D's values

>>> employee.values()
[35, 'Jatin', 'Pune']
>>> employee1=employee
>>> help({}.get)
Help on built-in function get:

get(...)
    D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.

>>> employee = {'emp1:6000','emp2':8000,'emp3':9000}
SyntaxError: invalid syntax
>>> employee = {'emp1':6000,'emp2':8000,'emp3':9000}
>>> sorted(employee.items(),key=lambda x:x[1],reverse=True)
[('emp3', 9000), ('emp2', 8000), ('emp1', 6000)]
>>> sorted(employee.items(),key=lambda x:x[1],reverse=True)[0][0]
'emp3'
>>> 
