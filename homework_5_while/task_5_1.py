# შეყვანილი n ნატურალური რიცხვამდე ყველა რიცხვის გამყოფის დაბეჭდვა (მაქს. 3 გამყოფი), სადაც 0<n<50

input_number = int(input("Please input number between 1 and 50: "))

i = 1
while i < input_number:
    print(f"{i} -", end=" ")
    j = 1
    count = 0
    
    while j <= i and count<3:
        if i % j == 0:
            print(j, end=" ")
            count += 1
        j = j +1
    print()
    i += 1

