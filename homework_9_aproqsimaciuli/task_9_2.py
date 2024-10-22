# pi 2
 
n = int(input("Please enter number greater than 1: "))

from random import uniform
from math import sqrt

counter = 0
for _ in range(n):
    a = uniform(0, 1)
    b = uniform(0, 1)
    if sqrt(a ** 2 + b ** 2) <= 1:
        counter += 1
print(4 * counter / n)

#10-3.2
#10000000 -- 3.1422084 ---> pi