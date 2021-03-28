def split(word):
    return[char for char in word]
word = input("Input your word")
newword = []
splitword = split(word)

for x in range(len(splitword)):
    if splitword[x] == "a":
        newword.append(splitword[x])
    elif splitword[x] == "o":
        newword.append(splitword[x])
    elif splitword[x] == "e":
        newword.append(splitword[x])
    elif splitword[x] == "i":
        newword.append(splitword[x])
    elif splitword[x] == "u":
        newword.append(splitword[x])
    else:
        temp = []
        temp.append(splitword[x])
        temp.append("o")
        temp.append(splitword[x])
        temp2 = ''.join(temp)
        newword.append(temp2)

print(''.join(newword))