
print 'Program started'

var = 10

def func(a,b):
    print 'Inside function'
    c = a + b
    return c

for i in range(2):
    print i

var2 = 20

func(var,var2)

name = 'jay'
if name == 'jay':
    print name
else:
    print 'you changed name'