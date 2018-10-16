class Car(object):

    def __init__(self, make, model):
        self.make = make
        self.model = model

c1 = Car('bmw','550i')
print(c1.make)
print(c1.model)

c2 = Car('benz', '550j')
print(c2.make)
print(c2.model)