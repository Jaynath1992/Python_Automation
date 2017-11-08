def function(a, *args, **kwargs):
    print "a:",a
    print "args:", args
    print "kwargs:",kwargs
    

function(10,20,30,d=40,c=20,b=30) 


#While passing any number of arguments in form of keyword and non keyword arguments
#NOn keywords arguments will get printed in form of tuples

# While Keyword arguments gets printed in form of dictionary


