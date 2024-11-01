# draw with while

inputed_number = int(input("Please enter a positive integer number between 1 and 9: "))

i = 1
while i <= inputed_number:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1

i = inputed_number - 1
while i > 0:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i -= 1
