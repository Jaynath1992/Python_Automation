#Function definition

function()
def function(a,b=20,c):
    print a
    print b
    print c
    print 'This is in line 1 in function'
    print 'This is line2 in function'
    return 'return value'
a= function()

print a


# If there is no return statement inside function ,then it returns None

# In function you can  not call function before defining it, because here interpretes line
#by line, and if it does not finds, then it will generate name error function not defined

function(a)  #Non Keyword argument
function(a=1)  #Keyword argument

function(b=1)  #then it will give error because no b parameter is defined

# values in passed by reference
# we can shuffle if we provide keyword argument

# 1. as per the rule in function, you can not have non keyword argument after keyword argument

function(a=10, 4)  # it will give error

function(10,b=4) #This will work

# 2. you can not have multiple values for a single argument

function(10,a=4) # Here passing a=10 but again passing a=4 so we can't do, error

# 3. You can not have non default argument after default argument


function(a=10, c=20)


# When passing n numer of non keywords arguments , then use like this
#passed inform of tuples


def function(a,*args):
    print a
    print args

function(0,[1,2,3],3)

#For passing n numebr of 

def function(a,**kwargs):
    print a
    print kwargs


function(a=10, b=20, c=30)


def function(a, *args, **kwargs):
    print "args:", args
    print "kwargs:",kwargs
    print "a:",a

function(10,20,30,d=40,c=20,b=30)   #Keyword arguments













