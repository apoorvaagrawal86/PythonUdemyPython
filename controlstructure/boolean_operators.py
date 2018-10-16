and_output1 = (10 == 10) and (10 > 9)
and_output2 = (10 == 10) and (10 < 9)
and_output3 = (10 > 10) and (10 < 9)

or_output1 = (10 == 10) or (10 > 9)
or_output2 = (10 == 10) or (10 < 9)
or_output3 = (10 > 10) and (10 < 9)

not_true = not(10 == 10)
not_false = not(10 > 10)

print(and_output1,and_output2,and_output3,or_output1,or_output2,or_output3,not_true,not_false)