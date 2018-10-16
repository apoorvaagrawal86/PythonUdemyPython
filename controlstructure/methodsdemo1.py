def sum_nums():
    print (3 + 2)

sum_nums()

def sum_num(a,b):
    print(a+b)

sum_num(4,5)

l = [1,2,3]
print(l.append(4))
print(l)

print(len(l))

def add_num(a,b):
    return a+b
sum1 = add_num(2,8)
sum2 = add_num(3,3)
print(sum1)
print(sum2)

def isMetro(city_name):
    l = ['sfo', 'nyc', 'la']
    if city_name in l:
        return True
    else:
        return False
x = isMetro('boston')
print(x)


def add_nums(n1=2, n2=4):
    return n1+n2

sum1 = add_nums()
print(sum1)

sum2 = add_nums(n1=12, n2=21)
print(sum2)

x = 10

def test_method(x):
    print("value of local x is: " + str(x))
    x = 2
    print("New value of local x is: " + str(x))

print("Value of global x is: " + str(x))
test_method(x)
print('Did the value of global x change? ' + str(a))

def test_method():
    global y
    print("value of 'y' inside the method is: " + str(y))
    y=2
    print("value of 'y' inside the method is changed to: " + str(y))

print("value of global y is: " + str(y))
test_method()
print("Did the value of global 'a' change? " + str(y))