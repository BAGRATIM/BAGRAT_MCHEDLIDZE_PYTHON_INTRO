# pi

n = int(input("Please enter number greater than 1: "))

sum1 = 0
i = 1
while i < 2 * n :
    sum1 = sum1 + 1/i
    i = i + 4

sum2 = 0
i = -3
while abs(i) < (2 * n):
    sum2 = sum2 + 1/i
    i = i - 4

print(4*(sum1+sum2))

# 10     3.0418396189294024
#100     3.131592903558553
#10000   3.141492653590049
#100000  3.1415826535897065  ---> pi