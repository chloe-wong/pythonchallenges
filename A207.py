numberofitems = int(input("How many items?"))
items = []
for x in range(numberofitems):
    a = input()
    items.append(a)
items = sorted(items)
file = open("filetostore.txt","w")
for x in range(len(items)):
    a = items[x] + '\n'
    file.write(a)