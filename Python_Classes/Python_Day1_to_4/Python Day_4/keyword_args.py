def function(a,*args):
    print 'a:', a
    print 'args:', args


#function(a=10,20,30,40)    #Here it will give error because we can not pass non keyword
#arguments after keyword arguments.Here a is keyword arg and rest are non keywords arg,so it willgive error (syntax error)


#Passing non- keyword args use *args(generally) in parameter
def function1(*args):
    print 'args:',args

#function1(10,20,30) # Here output will be in form of tuple of (10,20,30)

# When we are passing n number of non-keyword args, then use *args in parameter in function
# then it will return tuple of arguments

# Passing keyword args(named args)


def function2(**kwargs):
    print 'kwargs:', kwargs


#function2(a=10,b=20,c=30,d=40) # Here Ouptput- kwargs: {'a': 10, 'c': 30, 'b': 20, 'd': 40}

# If we have to pass named(keyword args) then use **kwargs(generally) as parameter to
#receive value of arguments, it will return dictionary in key value pairs


def function3(*args,**kwargs):
    print 'args:', args
    print 'kwargs', kwargs

#function3(10,20,30,40)  # Here output args=(10,20,30,40) and kwargs={}

#Because we are not passing any keyword arguments, above all are non-keyword arguments,
# that's why we are getting nothing in kwargs

#function3(10,20,30,a=40)    #args=(10,20,30), kwargs={'d':'40'}










