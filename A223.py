neat = []
def split(y):
    return[char for char in y]
for x in range(101,1000):
    y = str(x)
    temp = split(y)
    temp = list(map(int, temp))
    y = sum(temp)
    if x%y == 0:
        neat.append(x)
print(neat)