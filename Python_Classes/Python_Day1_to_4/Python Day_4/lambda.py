Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> employee = {'{'name':'jaynath'}':'pune'}
SyntaxError: invalid syntax
>>> employee = {{'name':'jaynath'}:'pune'}

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    employee = {{'name':'jaynath'}:'pune'}
TypeError: unhashable type: 'dict'
>>> {('name':'jaynath'):'pune'}
SyntaxError: invalid syntax
>>> {('name'):'pune'}
{'name': 'pune'}
>>> help(Xrange)

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    help(Xrange)
NameError: name 'Xrange' is not defined
>>> help(xrange)
Help on class xrange in module __builtin__:

class xrange(object)
 |  xrange(stop) -> xrange object
 |  xrange(start, stop[, step]) -> xrange object
 |  
 |  Like range(), but instead of returning a list, returns an object that
 |  generates the numbers in the range on demand.  For looping, this is 
 |  slightly faster than range() and more memory efficient.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __iter__(...)
 |      x.__iter__() <==> iter(x)
 |  
 |  __len__(...)
 |      x.__len__() <==> len(x)
 |  
 |  __reduce__(...)
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  __reversed__(...)
 |      Returns a reverse iterator.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T

>>> xrange(100)
xrange(100)
>>> 
= RESTART: C:/Users/Jaynath/Desktop/Python_Classes/Python Day_4/function.py =
This is in line 1 in function
This is line2 in function
>>> 
= RESTART: C:/Users/Jaynath/Desktop/Python_Classes/Python Day_4/function.py =
This is in line 1 in function
This is line2 in function
None
>>> 
= RESTART: C:/Users/Jaynath/Desktop/Python_Classes/Python Day_4/function.py =
This is in line 1 in function
This is line2 in function
return value
>>> 
= RESTART: C:/Users/Jaynath/Desktop/Python_Classes/Python Day_4/function.py =
This is in line 1 in function
This is line2 in function
return value
>>> 
= RESTART: C:/Users/Jaynath/Desktop/Python_Classes/Python Day_4/function.py =

Traceback (most recent call last):
  File "C:/Users/Jaynath/Desktop/Python_Classes/Python Day_4/function.py", line 3, in <module>
    function()
NameError: name 'function' is not defined
>>> 
== RESTART: C:/Users/Jaynath/Desktop/Python_Classes/Python Day_4/KW-NKW.py ==
args: (20, 30)
kwargs: {'c': 20, 'b': 30, 'd': 40}
a: 10
>>> 
== RESTART: C:/Users/Jaynath/Desktop/Python_Classes/Python Day_4/KW-NKW.py ==
a: 10
args: (20, 30)
kwargs: {'c': 20, 'b': 30, 'd': 40}
>>> 
 RESTART: C:/Users/Jaynath/Desktop/Python_Classes/Python Day_4/keyword_args.py 
a: 10
args: (20, 30, 40)
>>> 
 RESTART: C:/Users/Jaynath/Desktop/Python_Classes/Python Day_4/keyword_args.py 
a: 10
args: (20, 30)
>>> 
 RESTART: C:/Users/Jaynath/Desktop/Python_Classes/Python Day_4/keyword_args.py 

Traceback (most recent call last):
  File "C:/Users/Jaynath/Desktop/Python_Classes/Python Day_4/keyword_args.py", line 13, in <module>
    function1(10,20,30)
NameError: name 'function1' is not defined
>>> 
 RESTART: C:/Users/Jaynath/Desktop/Python_Classes/Python Day_4/keyword_args.py 
args: (10, 20, 30)
>>> 
 RESTART: C:/Users/Jaynath/Desktop/Python_Classes/Python Day_4/keyword_args.py 
kwargs: {'a': 10, 'c': 30, 'b': 20, 'd': 40}
>>> 
 RESTART: C:/Users/Jaynath/Desktop/Python_Classes/Python Day_4/keyword_args.py 
args: (10, 20, 30, 40)
kwargs {}
>>> 
 RESTART: C:/Users/Jaynath/Desktop/Python_Classes/Python Day_4/keyword_args.py 
args: (10, 20, 30)
kwargs {'a': 40}
>>> map(lambda x:x**3,range(1,11))kwargs: {'a': 10, 'c': 30, 'b': 20, 'd': 40}
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> def cube(x):
	return x ** 3

>>> map(cube,range(1,11))
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
>>> map(lambds x:x**3,range(1,11))
SyntaxError: invalid syntax
>>>  map(lambda x:x**3,range(1,11))
 
  File "<pyshell#17>", line 2
    map(lambda x:x**3,range(1,11))
    ^
IndentationError: unexpected indent
>>> map(lambda x:x**3,range(1,11))
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
>>> filter(cube,range(0,11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> help(filter)
Help on built-in function filter in module __builtin__:

filter(...)
    filter(function or None, sequence) -> list, tuple, or string
    
    Return those items of sequence for which function(item) is true.  If
    function is None, return the items that are true.  If sequence is a tuple
    or string, return the same type, else return a list.

>>> filter(lambds:x:x%2,range(1,100))
SyntaxError: invalid syntax
>>> filter(lambda:x:x%2,range(1,100))
SyntaxError: invalid syntax
>>> filter(lambda:x:x%2,range(1,100))
SyntaxError: invalid syntax
>>> filter(lambda x:x%2,range(1,100))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> 

>>> 
>>> notaprime = [i for i in range(2,10) for j in range(i*2,100,i)]
>>> print notaprime
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
>>>  notaprime = [j for i in range(2,10) for j in range(i*2,100,i)]
 
  File "<pyshell#29>", line 2
    notaprime = [j for i in range(2,10) for j in range(i*2,100,i)]
    ^
IndentationError: unexpected indent
>>> notaprime = [j for i in range(2,10) for j in range(i*2,100,i)]
>>> print notaprime
[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]
>>> [i for in range(2,100) if i not in notaprime]
SyntaxError: invalid syntax
>>> [i for i in range(2,100) if i not in notaprime]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
>>> [j for i in range(1,10) for j in i if i%2 ==1]

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    [j for i in range(1,10) for j in i if i%2 ==1]
TypeError: 'int' object is not iterable
>>> [j for i in range(1,10) for j in i if j%2 ==1]

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    [j for i in range(1,10) for j in i if j%2 ==1]
TypeError: 'int' object is not iterable
>>> [j for i in range(1,10) for j in i if j%2 ==1]

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    [j for i in range(1,10) for j in i if j%2 ==1]
TypeError: 'int' object is not iterable
>>> [j for i in range(1,10) for j in range(i) if j%2 ==1]
[1, 1, 1, 3, 1, 3, 1, 3, 5, 1, 3, 5, 1, 3, 5, 7, 1, 3, 5, 7]
>>> 
>>> 
>>> 
>>> names = ['Jatin','Akash','Vijay']
>>> dept = ['IT','HR','Admin']
>>> 
>>> {j for i in range(len(names)) print names}
SyntaxError: invalid syntax
>>> {j for i in range(len(names)) print names[i]}
SyntaxError: invalid syntax
>>> {j for i in range(len(names)) names[i]}
SyntaxError: invalid syntax
>>> {j for i in range(len(names)) names[i]}
SyntaxError: invalid syntax
>>> [j for i in range(len(names)) names[i]]
SyntaxError: invalid syntax
>>> for i in range(len(names))
SyntaxError: invalid syntax
>>> for i in range(len(names)):
	print dict(i,names[i])

	

Traceback (most recent call last):
  File "<pyshell#52>", line 2, in <module>
    print dict(i,names[i])
TypeError: dict expected at most 1 arguments, got 2
>>> for i in range(len(names)):
	print dict(names[i])

	

Traceback (most recent call last):
  File "<pyshell#54>", line 2, in <module>
    print dict(names[i])
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> dict(0=names[0],1=names[1],2=names[2])
SyntaxError: keyword can't be an expression
>>> dict(0=names[0],1=names[1],2=names[2])
SyntaxError: keyword can't be an expression
>>> 
>>> dict(i in range(len(names)) for in names)
SyntaxError: invalid syntax
>>> dict(i in range(len(names)) for i in names)

Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    dict(i in range(len(names)) for i in names)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> 
>>> {i:j for i,j in enumerate(names)}
{0: 'Jatin', 1: 'Akash', 2: 'Vijay'}
>>> {i:j for i in range(len(names) for j in names[i])}

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    {i:j for i in range(len(names) for j in names[i])}
TypeError: range() integer end argument expected, got generator.
>>> zip(names,dept)
[('Jatin', 'IT'), ('Akash', 'HR'), ('Vijay', 'Admin')]
>>> {i:j for i,j in zip(names,dept)}
{'Vijay': 'Admin', 'Jatin': 'IT', 'Akash': 'HR'}
>>> {i:j for i in range(len(names)) for j in names[i])}
SyntaxError: invalid syntax
>>> {i:j for i in range(len(names)) for j in names[i]}
{0: 'n', 1: 'h', 2: 'y'}
>>> names
['Jatin', 'Akash', 'Vijay']
>>> {i:j for i in range(len(names)) j = names[i]}
SyntaxError: invalid syntax
>>> {i:j for i in range(len(names)) j = names[i]}
SyntaxError: invalid syntax
>>> {i:j for i in range(len(names)) j in names[i]}
SyntaxError: invalid syntax
>>> help(zip)
Help on built-in function zip in module __builtin__:

zip(...)
    zip(seq1 [, seq2 [...]]) -> [(seq1[0], seq2[0] ...), (...)]
    
    Return a list of tuples, where each tuple contains the i-th element
    from each of the argument sequences.  The returned list is truncated
    in length to the length of the shortest argument sequence.

>>> zip(names,dept)
[('Jatin', 'IT'), ('Akash', 'HR'), ('Vijay', 'Admin')]
>>> location = ['pune','banglore','mumbai']
>>> zip(names,dept,location)
[('Jatin', 'IT', 'pune'), ('Akash', 'HR', 'banglore'), ('Vijay', 'Admin', 'mumbai')]
>>> 
