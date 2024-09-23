#მოთამეეშების რაოდენობის მიხედვით კამათლის გაგორების დაბეჭდვა

from random import choice

repeat_count = int(input("Please enter players quantity: "))

for i in range(repeat_count):
    print(choice(['1', '2', '3', '4', '5', '6']),":", choice(['1', '2', '3', '4', '5', '6']))