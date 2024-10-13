# reverse number and sum of digits

input_number = input("Please enter a positive integer number between 0 and 9999: ")

if len(input_number) == 1:
    print("reversed number is: ",input_number)
    print("sum of digits is: ",input_number)
elif len(input_number) == 2:
    print("reversed number is: ",input_number[1],input_number[0])
    print("sum of digits is: ",int(input_number[1])+int(input_number[0]))
elif len(input_number) == 3:
    print("reversed number is: ",input_number[2],input_number[1],input_number[0])
    print("sum of digits is: ",int(input_number[2])+int(input_number[1])+int(input_number[0]))
else:
    print("reversed number is: ",input_number[3],input_number[2],input_number[1],input_number[0])
    print("sum of digits is: ",int(input_number[3])+int(input_number[2])+int(input_number[1])+int(input_number[0]))
 
    