# მანქანის სიჩქარით მისი კატეგორიის განსაზღვრა

car_speed = float(input("გთხოვთ შეიყვანოთ მანქანის სიჩქარე კმ/სთ-ებში: "))

if car_speed <= 0 or car_speed > 500:
    print("მანქანაა? :)")

elif car_speed < 30:
    print("SLOW")    

elif car_speed > 120:
    print("VERY FAST")

elif car_speed > 60:
    print("FAST")

elif car_speed > 30:
    print("MODERATE")

else:
    print("check code")