import math
a=int(input("what is triangle's side A?: "))
b=int(input("what is triangle's side B?: "))
c=int(input("what is triangle's side C?: "))            
P=a+b+c

print("Area is: ",math.sqrt(P/2*(P/2-a)*(P/2-b)*(P/2-c)))  

print("perimeter is: ",P)