import math
from math import comb
a = int(input("Input the constant"))
b = int(input("Input the coefficient of x"))
c1 = int(input("Input the power"))
c = c1

print(a**c)
c = c-1
print((math.comb(c1,c))*(a**c)*(b**(c1-c)),"x")
c = c-1
for x in range(c1-1):
   coefficient = (math.comb(c1,c))*(a**c)*(b**(c1-c))
   print(coefficient,"x ^",(c1-c))
   c = c-1