array = [1,5,7,10,12]
minimum = 99999
for x in range(len(array)):
    for y in range(len(array)):
        if array[y] - array[x] > 0:
            if array[y]- array[x] < minimum:
                minimum = array[y]-array[x]
print(minimum)