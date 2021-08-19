n = int(input())
bulbs = []
for x in range(n):
    bulbs.append(0)
number = int(input())
for x in range(number):
    a = sorted(list(map(int,input().split())))
    start,end = a[0],a[1]
    for x in range(start,end+1):
        temp = bulbs[x]
        if temp == 0:
            bulbs[x] = 1
        elif temp == 1:
            bulbs[x] = 0
print(bulbs.count(1))