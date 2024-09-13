number = float(input("გთხოვთ შეიყვანოთ მთელი რიცხვი 1-დან 10-ის ჩათვლით: "))

if number < 1 or number > 10 or number % 1 != 0:
    print("შეყვანილი რიცხვი არ არის 1-დან 10-მდე მთელი რიცხვი")    
    exit(1)


elif number == 1 or number == 2 or number == 3 or number == 5 or number == 7:
    print(number, "არ არის შედგენილი რიცხვი")

elif number == 4:
    print("2, 2")
elif number == 6:
    print("2, 3")
elif number == 8:
    print("2, 2, 2")
elif number == 9:
    print("3, 3")
elif number == 10:
    print("2, 5")
else:
    print("check code")