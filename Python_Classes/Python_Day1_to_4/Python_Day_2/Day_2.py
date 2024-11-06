There are different types of data types in Python. Some built-in Python data types are:

Numeric data types: int, float, complex
String data types: str
Sequence types: list, tuple, range
Binary types: bytes, bytearray, memoryview
Mapping data type: dict
Boolean type: bool
Set data types: set, frozenset



Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 2**31
2147483648L
>>> type(21474836489)
<type 'long'>
>>> 2**63
9223372036854775808L
>>> 2**127
170141183460469231731687303715884105728L
>>> a = 3 + 4j
>>> type(a)
<type 'complex'>
>>> 10/3.0
3.3333333333333335
>>> 10.0/3
3.3333333333333335
>>> 10/3
3
>>> 10.0/3.0
3.3333333333333335
>>> 10**3
1000
>>> 10//3
3
>>> 10.0//3
3.0
>>> 10 % 2
0
>>> 11 % 3
2
>>> 10*2/3
6
>>>  #Operator Precedence and Operator associativity rule
>>> 10**2 + 30*2/3
120
>>> 10**2 +30*(2/3)
100
>>> bin(10)
'0b1010'
>>> bin(129)
'0b10000001'
>>> #first two character represents it is a binary number
>>> int('1001',2)
9
>>> 44>>3
5
>>> 11 & 15
11
>>> 11 | 15
15
>>> print '*'*10
**********
>>> 11 ^ 15
4
>>> 10 == 10.0
True
>>> 10 == int(10.1)
True
>>> 10 + '10'

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    10 + '10'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 10 + int('10')
20
>>> 
>>> str(10) + '10'
'1010'
>>> float(10)
10.0
>>> hex(10)
'0xa'
>>> abs(3+4j)
5.0
>>> #return type of complex is float
>>> cmp(1,2)
-1
>>> cmp(1,2)
-1
>>> cmp(1,1)
0
>>> cmp(2,1)
1
>>> cmp('jay','nath')
-1
>>> ('nath','jay')
('nath', 'jay')
>>> cmp('nath','jay')
1
>>> cmp('1','b')
-1
>>> cmp('b','10')
1
>>> cmp('b',66)
1
>>> cmp('b',98)
1
>>> cmp('a',91)
1
>>> cmp('a',64)
1
>>> cmp('a',103)
1
>>> isinstance(a,int)
False
>>> name = 'jatin'
>>> location = 'pune'
>>> location = "pune"
>>> paragraph = '''
this is line 1
this is line 2
this is line 3
'''
>>> type(name)
<type 'str'>
>>> name + location
'jatinpune'
>>> name **2

Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    name **2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> name * 2
'jatinjatin'
>>> print '**' * 20, '\nWelcome to Python Classes\n', '**' * 20
**************************************** 
Welcome to Python Classes
****************************************
>>> jatin != 'Jatin'

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    jatin != 'Jatin'
NameError: name 'jatin' is not defined
>>> 'jatin' >= 'Jatin'
True
>>> cmp(20,'j')
-1
>>> cmp(101,'j')
-1
>>> cmp(120,'j')
-1
>>> ord('j')
106
>>> cmp(120,'j')
-1
>>> chr(74)
'J'
>>> cmp('J',102)
1
>>> cmp('j',103)
1
>>> cmp(101,'j')
-1
>>> len('Jatin')
5
>>> len(int)

Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    len(int)
TypeError: object of type 'type' has no len()
>>> string = 'This is my string'
>>> 'is' in string
True
>>> 'is' not in string
False
>>> a= 10
>>> id(a)
40465956
>>> a=20
>>> id(q)

Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    id(q)
NameError: name 'q' is not defined
>>> id(a)
40465836
>>> name = 'nitin'
>>> name == name[::-1]
True
>>> name[6:1:-1]
'nit'
>>> name[12:1:-1]
'nit'
>>> name = 'jaynath'
>>> name[4:8:-1]
''
>>> name[8:4:-1]
'ht'
>>> name[8:4:-2]
'h'
>>> name[::]
'jaynath'
>>> name[4:]
'ath'
>>> name[:5]
'jayna'
>>> name[7:6:-1]
''
>>> name[4:2:-2]
'a'
>>> name[1::2]
'ant'
>>> name = 235534
>>> name[0]

Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    name[0]
TypeError: 'int' object has no attribute '__getitem__'
>>> chr(10)
'\n'
>>> chr(6)
'\x06'
>>> chr(10)
'\n'
>>> name = ['Jatin','Akash','Vijay','Mohan']
>>> len(names)

Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    len(names)
NameError: name 'names' is not defined
>>> len(name)
4
>>> name[0]
'Jatin'
>>> name[-1]
'Mohan'
>>> names = [4] ='Vaibhav'
SyntaxError: can't assign to literal
>>> name[4] = 'Vaibhav'

Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    name[4] = 'Vaibhav'
IndexError: list assignment index out of range
>>> name[3] = 'Raj'
>>> names

Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    names
NameError: name 'names' is not defined
>>> name
['Jatin', 'Akash', 'Vijay', 'Raj']
>>> name[3] = 'Mohan'
>>> name
['Jatin', 'Akash', 'Vijay', 'Mohan']
>>> name2=name
>>> name2
['Jatin', 'Akash', 'Vijay', 'Mohan']
>>> name2[0] = 'Rahul'
>>> name
['Rahul', 'Akash', 'Vijay', 'Mohan']
>>> name2
['Rahul', 'Akash', 'Vijay', 'Mohan']
>>> #This is called as Deep Copy in Python
>>> id(name)
51119288
>>> id(name2)
51119288
>>> name2 =2
>>> name2
2
>>> name
['Rahul', 'Akash', 'Vijay', 'Mohan']
>>> id(name2)
40466052
>>> id(name)
51119288
>>> #When you are assigning some other values to name2 then it's previous memory location gates destroyed and it creates under a new mwmory location.
>>> 
