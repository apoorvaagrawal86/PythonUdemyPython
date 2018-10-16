my_list = [1,2,3]
print(my_list)

my_list[0] = 0
print(my_list)

my_tuple = (1, 2, 3)
print(my_tuple)

#my_tuple[0] = 0
print(my_tuple[0])

print(my_tuple[1:])
print(my_tuple[:1])
print(my_tuple[1:2])
print(my_tuple.index(1))
print(my_tuple.count(2))

new_tuple = (1,2,3,2,3,4,2,3,2,2,3)
print(new_tuple.count(2))
print(new_tuple.count(3))

#count and index are the only two methods available in tuple.
#Difference between tuple and list is that list is mutable and tuple is immutable.