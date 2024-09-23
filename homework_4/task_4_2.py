# n ცალი შემთხვევითი რიცხვიდან მაქსიმუმის პოვნა, სადაც 0<n<30, 0<შემთხვევითი რიცხვი<1000

import random

input_number = input("Please enter a positive integer number between 1 and 29: ")

float_input_number = float(input_number)
int_input_number = int(float_input_number)

#checks
if int_input_number <=0:
    print("Please enter positive number")
    exit(1)
elif int_input_number >=30:
     print("Please enter number less then 30")
     exit(1)
elif float_input_number != int_input_number:
    print("Please enter integer number")
    exit(1)
else:
    print(int_input_number)

#code
max_number=0
for i in range(int_input_number):
        number = random.randint(0, 1000)
        print("Generated number: ", number)
        
        if number > max_number:
            max_number = number
print("maximum number is", max_number)


