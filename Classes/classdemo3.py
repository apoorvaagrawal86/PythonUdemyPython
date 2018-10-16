class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print("make of the car: " + self.make)
        print("model of the car: " + self.model)

print(Car.wheels)
c1 = Car('bmw', '550i')
print(c1.make)
c1.wheels = 3
print(c1.wheels)
print(Car.wheels)
c1.info()


c2 = Car('benz', 'E350')
#print(c2.wheels)
print(c2.make)
c1.info()
print(Car.wheels)