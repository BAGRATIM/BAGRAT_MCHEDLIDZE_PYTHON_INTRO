'''
Დაწერეთ ფუნქცია რომელიც დაითვლის რიცხვის ფაქტორიალს. 
Გამოიძახეთ ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტისთვის რომ აჩვენოთ მისი მუშაობა
'''

def faqtoriali(number):
    i = 1
    mult = 1
    while i <= number:
        mult = mult*i
        i += 1
    print(f"{number}!= {mult}")


faqtoriali(3)
faqtoriali(5)
faqtoriali(6)