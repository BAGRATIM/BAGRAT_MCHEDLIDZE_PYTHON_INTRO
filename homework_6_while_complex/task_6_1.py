# პროგრამის ჩაფიქრებული რიცხვის და იუზერის რიცხვების შედარება 10 ცდით
import random

number = random.randint(0, 100)
inputed_number = int(input("Enter the number: "))

try_counter=0
while try_counter < 10:
    #print(number)
    try_counter += 1
    if inputed_number > number:
        print("high")
        inputed_number = int(input("Enter the number: "))
    elif inputed_number < number:
        print("low")
        inputed_number = int(input("Enter the number: "))
    else:
        print("You are a winner")
        break