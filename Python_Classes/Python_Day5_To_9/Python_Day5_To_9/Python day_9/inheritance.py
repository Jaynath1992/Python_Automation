# inheritance means we are borrowing functionalities

from myCar import Car

class euroCar(Car):

    def move_car(self, direction):
        print 'euro car is moving towards {}'.format(direction)

class AmericanCar(Car):
    def move_car(self, direction):
        print 'American car is moving towards {}'.format(direction)
        super(AmericanCar, self).move_car(direction)

# super is used to make call of parent class functionality
class IndianCar(euroCar,AmericanCar):
    pass
    #def move_car(self, direction):
    #    print 'Indian car is moving towards {}'.format(direction)


#audi = euroCar()
#audi.move_car('left')
audi = IndianCar()

audi.move_car('left')



# Multiple inheritance : always move from left to right for function overriding
