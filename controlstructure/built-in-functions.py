def largest_num(*args):
    print(max(args))
    return(max(args))

largest_num(-20,-10,0,10,100)
x = largest_num(-20,-10,0,10,100)
print(x)

def smallest_num(*args):
    return(min(args))

y = smallest_num(-20,-10,0,10,100)
print(y)

def abs_function(a):
    print(abs(a))

abs_function(-20)
abs_function(20)

print(type(99))
print(type(99.99))
print(type("99.99"))