'''
Დაწერეთ ფუნქცია, რომელიც დაადგენს გადაცემული რიცხვი მარტივია თუ არა. 
Გამოიძახეთ ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტისთვის რომ აჩვენოთ მისი მუშაობა
'''
def martivi(number):
    for i in range(2, number):
        if number % i == 0:
            print("no")
            exit(0)
    print("YES")

martivi(5)
martivi(7)
martivi(8)