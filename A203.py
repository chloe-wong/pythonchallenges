import random

def GenerateList():
    array = []
    for x in range(9):
        array.append(random.randint(1,1000))
    return(array)

def InsertionSort(array):
    for x in range(1, len(array)):
        current = array[x]
        position = x - 1
        while position >= 0 and current < array[position]:
            array[position + 1] = array[position]
            position -= 1
        array[position + 1] = current
