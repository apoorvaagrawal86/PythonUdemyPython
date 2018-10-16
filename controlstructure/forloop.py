my_string = 'abcabc'

for c in my_string:

    if c == 'a':
        print('A', end=' ')
    else:
        print(c, end=' ')

cars = ['bmw', 'benz', 'honda']
#print(cars)

for car in cars:
    print(car)

nums = [1,2,3]
for n in nums:
    print(n*10)

d = {'one':1, 'two':2, 'three':3}
for k in d:
    print(k)
    print(k + ' ' + str(d[k]))

for k,v in d.items():
    print(k,v)