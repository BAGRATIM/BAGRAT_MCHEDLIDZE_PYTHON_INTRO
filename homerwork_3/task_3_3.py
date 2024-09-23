#შეყვანილი დაბადების დღის თარიღის მიხედვით კვირის დღის დაბეჭდვა

from datetime import datetime

def birth_day_of_week():
    year = int(input("შეიყვანეთ თქვენი დაბადების წელი: "))
    month = int(input("შეიყვანეთ თქვენი დაბადების თვე რიცხვით ფორმატში: "))
    day = int(input("შეიყვანეთ თქვენი დაბადების დღის რიცხვი: "))
    
    birth_date = datetime(year, month, day)
    
    day_of_week = birth_date.strftime("%A")
        
    print("You were born on a",day_of_week)

birth_day_of_week()
