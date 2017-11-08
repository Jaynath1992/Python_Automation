Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import datetime
>>> dir(datetime)
['MAXYEAR', 'MINYEAR', '__doc__', '__name__', '__package__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'tzinfo']
>>> now = datetime.datetime.now()
>>> now
datetime.datetime(2017, 6, 10, 2, 28, 10, 363000)
>>> prit now
SyntaxError: invalid syntax
>>> print now
2017-06-10 02:28:10.363000
>>> older = datetime.datetime(2017,1,1,0,0,0,0)
>>> print older
2017-01-01 00:00:00
>>> now - older
datetime.timedelta(160, 8890, 363000)
>>> print now - older
160 days, 2:28:10.363000
>>> 
