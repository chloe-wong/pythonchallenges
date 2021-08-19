decimalvalues = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
romanvalues = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
def num_to_roman(x):
    temp = []
    y = 0
    a = ""
    while True:
        if x == 0:
            break
        else:
            flag = False
            while flag == False:
                if x - decimalvalues[y] >= 0:
                    x = x - decimalvalues[y]
                    temp.append(romanvalues[y])
                    flag = True
                else:
                    y = y+1
    a = "".join(temp)
    return(a)

def split(x):
    return[char for char in x]
def roman_to_num(x):
    xlist = split(x)
    alist = []
    value = 0
    while xlist != []:
        if len(xlist) == 1:
            if xlist[0] == "M":
                value = value + 1000
                xlist.pop(0)
            elif xlist[0] == "D":
                value = value + 500
                xlist.pop(0)
            elif xlist[0] == "C":
                    value = value + 100
                    xlist.pop(0)
            elif xlist[0] == "X":
                    value = value + 10
                    xlist.pop(0)
            elif xlist[0] == "L":
                value = value + 50
                xlist.pop(0)
            elif xlist[0] == "I":
                    value = value + 1
                    xlist.pop(0)
            elif xlist[0] == "V":
                value = value + 5
                xlist.pop(0)
        else:
            if xlist[0] == "M":
                value = value + 1000
                xlist.pop(0)
            elif xlist[0] == "D":
                value = value + 500
                xlist.pop(0)
            elif xlist[0] == "C":
                if xlist[1] == "M":
                    value = value + 900
                    xlist.pop(0)
                    xlist.pop(0)
                elif xlist[1] == "D":
                    value = value + 400
                    xlist.pop(0)
                    xlist.pop(0)
                else:
                    value = value + 100
                    xlist.pop(0)
            elif xlist[0] == "X":
                if xlist[1] == "C":
                    value = value + 90
                    xlist.pop(0)
                    xlist.pop(0)
                elif xlist[1] == "L":
                    value = value + 40
                    xlist.pop(0)
                    xlist.pop(0)
                else:
                    value = value + 10
                    xlist.pop(0)
            elif xlist[0] == "L":
                value = value + 50
                xlist.pop(0)
            elif xlist[0] == "I":
                if xlist[1] == "X":
                    value = value + 9
                    xlist.pop(0)
                    xlist.pop(0)
                elif xlist[1] == "V":
                    value = value + 4
                    xlist.pop(0)
                    xlist.pop(0)
                else:
                    value = value + 1
                    xlist.pop(0)
            elif xlist[0] == "V":
                value = value + 5
                xlist.pop(0)
    return(value)
