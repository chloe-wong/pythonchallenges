text = input()
a = int(input("Are the words space separated? 1 for yes, 2 for no"))
def split(text):
    return[char for char in text]
if a == 1:
    words = text.split()
    if "qwerty" in words:
        print("qwerty is present")
    else:
        print("qwerty is not present")
else:
    words = split(text)
    b = len(words) - 6
    flag = False
    for x in range(b):
        if (words[x] == "q") and (words[x+1] == "w") and (words[x+2] == "e") and (words[x+3] == "r") and (words[x+4] == "t") and (words[x+5] == "y"):
            flag = True
            break
    if flag == False:
        print("qwerty is not present")
    elif flag == True:
        print("qwerty is present")