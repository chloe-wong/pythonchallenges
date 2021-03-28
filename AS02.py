item = int(input("what integer would you like to find?"))
array = []
index = -1
for x in range(len(array)):
    if array[x] == item:
        index = x
        break
if index == -1:
    print("item is not found")
else:
    print("item found at location,"index)