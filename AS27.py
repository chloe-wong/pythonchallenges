file = open("10000words.txt","r")
array = []
for line in file:
    array.append(line.strip('\n'))
ordered = []
a = array[0]
for x in range(10000):
    print(a)
    lastchara = a[-1:]
    aindex = array.index(a)
    array.pop(aindex)
    y = 0
    firstcharb = "string"
    while True:
        if firstcharb == lastchara:
            a =  b
            break
        else:
            b = array[y]
            firstcharb = b[0]
            y = y+1