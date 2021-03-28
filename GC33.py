flag = False
calories = 0
reccalories = 2000
daycounter = 1
while flag == False:
    print("Day", daycounter)
    user = input("Input 'end day' to reset or 'continue' to continue")
    if user == "end day":
        print("You consumed:", calories)
        print("You should consume:",reccalories,"daily")
        calories = 0
        print("Calories reset to 0")
        daycounter = daycounter + 1
    else:
        food = input("Input food")
        cals = int(input("Input calories"))
        calories = calories + cals

