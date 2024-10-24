'''
Დაწერეთ ფუნქცია რომელიც არგუმენტად მიიღებს ტექსტს და დაარუნებს ამ ტექსტში ხმოვნების რაოდენობას. 
Გამოიძახეთ ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტისთვის რომ აჩვენოთ მისი მუშაობა
'''

def count_vowels(inputed_text):
    #inputed_text = input("Please input text: ")
    new_text = inputed_text.replace("a", "").replace("e", "").replace("i", "").replace("o", ""). replace("u", "")
    answer =  len(inputed_text)-len(new_text)
    print(f"Number of vowels in text is: {answer}")

count_vowels("chventvis")
count_vowels("es")
count_vowels("martivi")
count_vowels("operaciaa")