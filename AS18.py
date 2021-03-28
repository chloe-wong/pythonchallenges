#exercise 1
def turn_clockwise(x):
    if x == "N":
        return("E")
    elif x == "E":
        return("S")
    elif x == "S":
        return("W")
    elif x == "W":
        return("N")
    else:
        return(None)

#exercise 2
def day_name(x):
    if x == 0:
        return("Sunday")
    elif x == 1:
        return("Monday")
    elif x == 2:
        return("Tuesday")
    elif x == 3:
        return("Wednesday")
    elif x == 4:
        return("Thursday")
    elif x == 5:
        return("Friday")
    elif x == 6:
        return("Saturday")
    else:
        return(None)
x = int(input())
print(day_name(x))

#exercise 3
def day_name(x):
    if x == "Sunday":
        return(0)
    elif x == "Monday":
        return(1)
    elif x == "Tuesday":
        return(2)
    elif x == "Wednesday":
        return(3)
    elif x == "Thursday":
        return(4)
    elif x == "Friday":
        return(5)
    elif x == "Saturday":
        return(6)
    else:
        return(None)
x = input()
print(day_name(x))
