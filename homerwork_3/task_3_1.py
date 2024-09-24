# x-ის y ხარისხად აყვანა math.pow() ფუნქციის გამოყენებით  

from math import pow

def multiply_x_y_times():
    x = float(input("Enter the value of x: "))
    y = float(input("Enter the value of y: "))
    
    print(x, "to the power of", y, "equl to", pow(x,y))

multiply_x_y_times()
