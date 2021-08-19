#exercise1
a = []
odd = 0
x = 0
while True:
    print("type 'stop' to end input")
    x = input()
    if x == "stop":
        break
    else:
        a.append(x)
a = list(map(int,a))
for x in range(len(a)):
    if a[x]%2 != 0:
        odd = odd+1
print(odd)

#exercise2
a = []
even = []
x = 0
while True:
    print("type 'stop' to end input")
    x = input()
    if x == "stop":
        break
    else:
        a.append(x)
a = list(map(int,a))
for x in range(len(a)):
    if a[x]%2 == 0:
        even.append(a[x])
print(sum(even))

#exercise3
a = []
neg = []
x = 0
while True:
    print("type 'stop' to end input")
    x = input()
    if x == "stop":
        break
    else:
        a.append(x)
a = list(map(int,a))
for x in range(len(a)):
    if a[x] < 0:
        neg.append(a[x])
print(sum(neg))

#exercise4
a = []
five = 0
x = "lol"
while True:
    print("type 'stop' to end input")
    x = input()
    if x == "stop":
        break
    else:
        a.append(x)
for x in range(len(a)):
    if len(a[x]) == 5:
        five = five+1
print(five)

#exercise5
a = []
temp = []
x = 0
while True:
    print("type 'stop' to end input")
    x = input()
    if x == "stop":
        break
    else:
        a.append(x)
a = list(map(int,a))
for x in range(len(a)):
    if a[x]%2 == 0:
        break
    else:
        temp.append(a[x])
print(sum(temp))

#exercise6
a = []
count = 0
x = 0
while True:
    print("type 'stop' to end input")
    x = input()
    if x == "stop":
        break
    else:
        a.append(x)
for x in range(len(a)):
    if a[x] == "sam":
        break
    else:
        count = count+1
print(count)

#exercise7
def sqrt(n):
    approx = n/2.0
    while True:
        print("better")
        better = (approx + n/approx)/2.0
        if abs(approx - better) < 0.001:
            return better
        approx = better
sqrt(25)       #"better" printed 5 times, which is sqrt 25

#exercise9
def print_triangular_numbers(n):
    array = []
    for x in range(1,n+1):
        temp = []
        temp.append(x)
        a = int((x*(x+1))/2)
        temp.append("      ")
        temp.append(a)
        temp = list(map(str,temp))
        array.append("".join(temp))
    for x in range(len(array)):
        print(array[x])
print_triangular_numbers(5)

#exercise10
def is_prime(n):
    ans = True
    for x in range(2,n):
        if n%x == 0:
            ans = False
            break
    return(ans)
print(is_prime(35))
