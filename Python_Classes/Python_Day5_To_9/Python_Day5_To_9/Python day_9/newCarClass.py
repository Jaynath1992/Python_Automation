class Car(object):
    steeringType = 'Manual'

    @staticmethod       # Now this method is static , we can call it using class.methodname or using object also
    def moveSteering(direction):
        print 'Car is moving towards {} direction'.format(direction)


audi = Car()
audi.moveSteering('Left')
Car.moveSteering('Right')


