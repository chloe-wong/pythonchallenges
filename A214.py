#exercise1
dictionary = {}
sentence = input()
b = sentence.lower()
a = b.replace(" ","")

for x in range(len(a)):
    if a[x] in dictionary:
        dictionary[a[x]] = dictionary[a[x]]+1
    else:
        dictionary[a[x]] = 1
dictionaryitems = list(dictionary.items())
dictionaryitems.sort()
for y in range(len(dictionaryitems)):
    print(dictionaryitems[y])

#exercise2
a) 35: asks for value of bananas in d
b) 4: the program added an item, so there are now 4 in d
c) True: checked if grapes were a key in d
d) KeyError: 'pears': pears are not in d
e) 0: since pears are not in d, the program returns 0
f) ['apples', 'bananas', 'grapes', 'oranges']: returns the keys of d in alphabetical order
g) False: apples have been deleted so are no longer in d

def add_fruit(inventory, fruit, quantity=0):
    inventory[fruit] = quantity
    return

#exercise3
towrite = open("alice_words.txt",w)
toread = open("aliceplain.txt",r)
count = {}
for line in toread:
    a = line.split()
    for x in range(len(a)):
        if a[x] in dictionary:
            dictionary[a[x]] = dictionary[a[x]]+1
        else:
            dictionary[a[x]] = 1
dictionaryitems = list(dictionary.items())
dictionaryitems.sort()
for y in range(len(dictionaryitems)):
    print(dictionaryitems[y])
    towrite.append(dictionaryitems[y])



