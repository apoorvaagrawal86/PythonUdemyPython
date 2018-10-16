bool_output = True or not False and False
print(bool_output)

#Precedence order - not, and, or

bool_output1 = 10 == 10 or not 10 > 10 and 10 > 10
print(bool_output1)

bool_output2 = (10 == 10 or not 10 > 10) and 10 > 10
print(bool_output2)

