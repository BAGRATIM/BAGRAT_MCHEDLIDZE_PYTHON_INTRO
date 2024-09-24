# n სიმაღლის ნაძვის ხის დახატვა

n = int(input("Enter the height of the Christmas tree between 1 and 50: "))

if 0 > n or n> 50:
    print("Please enter number between 1 and 50.")
    exit(1)
print(' ' * (n-1) + '*')   
i = 0
while i < n:
    print(' ' * (n - i-1) + '/' * (i) + '|'+(i) *'\\')
    i += 1
print(' ' * (n-1) + '|')


    


