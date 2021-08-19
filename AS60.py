nn, mm = int(input()), int(input())
n,m = nn**0.5,mm**0.5
width = int(n*m)
print(width)
check = []
if width%2 == 0:
    for x in range(width):
        print(x)
        temp = []
        if x%2 == 0:
            for y in range(int(width/2)):
                temp.append(".")
                temp.append("*")
        elif x%2 != 0:
            for y in range(int(width/2)):
                temp.append("*")
                temp.append(".")
        check.append(temp)
else:
    for x in range(width):
        print(x)
        temp = []
        if x%2 == 0:
            for y in range(int(width/2)):
                temp.append(".")
                temp.append("*")
            temp.append(".")
        elif x%2 != 0:
            for y in range(int(width/2)):
                temp.append("*")
                temp.append(".")
            temp.appemd("*")
        check.append(temp)
for x in range(width):
    temp = "".join(check[x])
    print(temp)