print("Welcome to the ISBN 13 Check Digit Calculator.")
a = int(input("Input first digit"))
b = int(input("Input second digit"))
c = int(input("Input third digit"))
d = int(input("Input fourth digit"))
e = int(input("Input fifth digit"))
f = int(input("Input sixth digit"))
g = int(input("Input seventh digit"))
h = int(input("Input eighth digit"))
i = int(input("Input ninth digit"))
j = int(input("Input tenth digit"))
k = int(input("Input eleventh digit"))
l = int(input("Input twelvth digit"))

b1 = b*3
d1 = d*3
f1 = f*3
h1 = h*3
j1 = j*3
l1 = l*3

sum = (a + b1 + c + d1 + e + f1 + g + h1 + i + j1 + k + l1)
p = sum%10
check = 10 - p
print(check)