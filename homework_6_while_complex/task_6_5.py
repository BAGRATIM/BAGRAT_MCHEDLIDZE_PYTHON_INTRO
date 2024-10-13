#nadzvis xe cifrebit

n = int(input("Enter a number (0 < number < 9): "))

if n <= 0 or n >= 9:
    print("Invalid input. Please enter a number between 1 and 8.")
    exit(1)
i = 0
while i <= n:
    spaces = n - i
    while spaces > 0:
        print(" ", end="")
        spaces -= 1
    j = i
    while j >= 0:
        print(j, end="")
        j -= 1
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
        
    print()
    i += 1
