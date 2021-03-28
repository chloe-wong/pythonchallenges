#exercise 1
a,b,c,d,e,f,g,h,i,j = "all", "work", "and", "no", "play", "makes", "Jack", "a", "dull", "boy"
print(a+" "+b+" "+c+" "+d+" "+e+" "+f+" "+g+" "+h+" "+i+" "+j+" ")

#exercise 2
6*(1-2)

#exercise 4
bruce = 6
print(bruce + 4)

#exercise 5
P = 10000
n = 12
r = 0.08
t = int(input("input number of years"))
A = 1 + (r/n)
A = A**(n*t)
A = A*P
print(A)

#exercise 6
error: numbers cannot be divided by 0

#exercise 8
x = int(input("what is the current time? ex. 2200 or 0800"))
y = int(input("how many hours to wait?"))
if y < 24:
    z = y*100
    ans = x+z
elif y == 24:
    ans = x
else:
    z = y%24
    z = z*100
    ans = x+z
print(ans)