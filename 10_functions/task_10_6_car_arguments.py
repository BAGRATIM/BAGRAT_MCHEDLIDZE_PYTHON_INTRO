'''
Დაწერეთ ფუნქცია რომელსაც გადაეცემა მანქანის მწარმოებელი და გამოშვების წელი. 
Მანქანის მწარმოებელი უნდა იყოს აუცილებელი არგუმენტი, 
ხოლო გამოშვების წელის ნაგულისხმევი მნიშვნელობა უნდა იყოს მიმდინარე წელი. 
Ფუნქციას უნდა ჰქონდეს შესაძლებლობა, რომ გადაეცეს განუზღვრელი დასახელების და რაოდენობის კონფიგურაციის პარამეტრები. 
Გამოიძახეთ ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტისთვის რომ აჩვენოთ მისი მუშაობა
'''

def car(car_manufacturer, year = 2024, *args, **kwargs):
    print("car_manufacturer:", car_manufacturer)
    print("year:", year)
    if args:
        print("Extras:")
        for extra in args:
            print("\t", extra)

    if kwargs:
        print("Special instructions:")
        for key, value in kwargs.items():
            print(f"\t{key}: {value}")

car("Mercedes", 2023)
print("*" * 50)
car("FORD MUSTANG", 1967)
print("*" * 50)
car("TESLA", 2024)