x = input()
def split(x):
    return[char for char in x]
xlist = split(x)
nums = ['0','1','2','3','4','5','6','7','8','9','10']
signs=['+','-','/','*','^']
index = []
for x in range(len(xlist)):
    if xlist[x] in nums:
        index.append(xlist[x])
    elif xlist[x] in signs:
        index.append(xlist[x])
for x in range(len(index)):
    xlist.remove(index[x])
if len(xlist)%2 != 0:
    print("Brackets are not balanced")
else:
    a = len(xlist)-1
    flag = True
    for x in range(int(len(xlist)/2)):
        b = a-x
        if xlist[x] == "(":
            if xlist[b] != ")":
                print("Brackets are not balanced")
                flag = False
                break
        if xlist[x] == "{":
            if xlist[b] != "}":
                print("Brackets are not balanced")
                flag = False
                break
        if xlist[x] == "[":
            if xlist[b] != "]":
                print("Brackets are not balanced")
                flag = False
                break
if flag == True:
    print("Brackets are balanced")