#ლუწი/2 კენტო/3 სანამ !=1

input_number = input("Please enter a positive integer number between 1 and 1000: ")

float_input_number = float(input_number)
int_input_number = int(float_input_number)

#checks
if int_input_number <=0:
    print("Please enter positive number")
    exit(1)
elif int_input_number >1000:
     print("Please enter number less then 1000")
     exit(1)
elif float_input_number != int_input_number:
    print("Please enter integer number")
    exit(1)

new_number=int_input_number
while new_number !=1:
    print(new_number, end='-> ')
    if new_number % 2 == 0:
        new_number = new_number/2
    else:
        new_number = new_number * 3 + 1
print(new_number)         

