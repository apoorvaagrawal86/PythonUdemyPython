class Fruit(object):
    def __init__(self):
        print('This is the constructor')

    def nutrition(self):
        print('This is the nutrition method')

    def fruit_shape(self):
        print('This is the fruit shape method')


class BaseFruit(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print("Child Class Constructor")

    def nutrition(self):
        print("This is the child class nutrition method")

    def color(self):
        print("This is the child class color method")

F1 = Fruit()
F1.nutrition()
F1.fruit_shape()

F2 = BaseFruit()
F2.color()
F2.fruit_shape()