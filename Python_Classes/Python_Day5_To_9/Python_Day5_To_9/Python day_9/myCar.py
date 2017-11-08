class Car(object):
    no_of_tyres = 6

    def __init__(self, no_of_tyres =5):
        self.no_of_tyres = no_of_tyres

    def __del__(self):      # destructor : destroying objects
        print 'Destroying an object of the class'

    def move_car(self, direction):
        print 'car is moving towards {} direction'.format(direction)


    def set_no_of_tyres(self, count):
        self.no_of_tyres = count

    def get_no_of_tyres(self):
        return self.no_of_tyres

    def moveSteering(self,direction):
        self.direction = direction
        print 'car is moving towards {} direction'.format(direction)

if __name__ == '__main__':
    ciaz = Car(no_of_tyres=5)
    wagonR = Car(4)

    print ciaz.no_of_tyres
    print wagonR.no_of_tyres

#ciaz = Car()        # ciaz is a object od Car class
#ciaz2 = Car()       # again ciaz2 is a object of Car class

'''
ciaz.no_of_tyres = 10   # set attribute no_of_tyres = 10, this change would be only in ciaz object not ciaz2
print ciaz.no_of_tyres

Car.no_of_tyres = 5     # static attribute , using classname.attribute_name, here changes would be reflected to all objects

print  ciaz2.no_of_tyres
print Car.function1()

'''

#ciaz = Car()
#ciaz.moveSteering(direction='right')

# Here ciaz will be passed to self parameter in the function, and 2nd parameter would be direction

# attributes ar bydefault static but methods are non static , they are dynamic , u cant access function/methods
# with help of Class.methodname() - not possibel will throw error
# However you can access attributes with help of class.attribute_name,and object.attribute_name, because by default attributes are staic

#wagonR = Car()
#wagonR.moveSteering('left')

# self is a parameter in a function inside class whose value will be object calling that function

#ciaz.set_no_of_tyres(5)
#wagonR.set_no_of_tyres(4)

#print ciaz.get_no_of_tyres()
#print wagonR.get_no_of_tyres()

