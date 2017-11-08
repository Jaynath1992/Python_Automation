Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import allOperations.arithmatic
>>> allOperations.arithmatic.add(10,20)
30
>>> import allOperations.arithmatic as pm
>>> pm.add(10,20)
30
>>> from allOperation import arithmatic

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    from allOperation import arithmatic
ImportError: No module named allOperation
>>> from allOperations.arithmatic import *
>>> add(10,20)
30
>>> 
=============================== RESTART: Shell ===============================
>>> from allOperations import arithmatic,arithmatic2
>>> arithmatic2.sub(30,10)
20
>>> from allOperations import *
>>> arithmatic2.add(10,20)
30
>>> from allOperations.arithmatic2
SyntaxError: invalid syntax
>>> from allOperations.arithmatic2 import add
>>> add(20,30)
50
>>> 
=============================== RESTART: Shell ===============================
>>> from allOperations import *
>>> arithmatic.add(10,20)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    arithmatic.add(10,20)
NameError: name 'arithmatic' is not defined
>>> from allOperations import *
>>> arithmatic2.add(10,20)

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    arithmatic2.add(10,20)
NameError: name 'arithmatic2' is not defined
>>> arithmatic.add(10,20)

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    arithmatic.add(10,20)
NameError: name 'arithmatic' is not defined
>>> 
=============================== RESTART: Shell ===============================
>>> from allOperations import *
>>> arithmatic.add(10,20)
30
>>> arithmatic2.add(10,20)
30
>>> 
=============================== RESTART: Shell ===============================
>>> from allOperations.cmpOperations import arithmatic2
>>> add(10,20)

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    add(10,20)
NameError: name 'add' is not defined
>>> arithmatic2.add(10,20)
30
>>> 
