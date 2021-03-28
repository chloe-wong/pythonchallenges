from collections import Counter
t = input("Input your text")
twords = t.split()
def split(y):
    return[char for char in y]
letters = []
for x in range(len(twords)):
    y = twords[x]
    temp = split(y)
    for z in range(len(temp)):
        letters.append(temp[z])
biggest = []
biggest.append(max(letters,key = letters.count))
letters = [x for x in letters if x != (max(letters,key=letters.count))]
biggest.append(max(letters,key = letters.count))
letters = [x for x in letters if x != (max(letters,key=letters.count))]
biggest.append(max(letters,key = letters.count))
letters = [x for x in letters if x != (max(letters,key=letters.count))]
for x in range(3):
    print(biggest[x])