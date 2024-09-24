# ყველა გამყოფის ერთ სიაში დაბეჭდვა

input_number = input("Please enter a positive integer number between 1 and 1000: ")

float_input_number = float(input_number)
int_input_number = int(float_input_number)

#checks
if int_input_number <=0:
    print("Please enter positive number")
    exit(1)
elif int_input_number >=1000:
     print("Please enter number less then 1000")
     exit(1)
elif float_input_number != int_input_number:
    print("Please enter integer number")
    exit(1)

for i in range(1, int_input_number+1):
       if int_input_number % i == 0:
            print(i, end=' ')




