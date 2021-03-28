from random import randint
array = []
for x in range(50):
    value = randint(0,1000000000)
    array.append(value)
print("the minimum is:",min(array))
print("the maximum is",max(array))
print("the average is:",(sum(array))/50)