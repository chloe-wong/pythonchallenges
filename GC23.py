name1, name2 = input("Input Team 1 Name"), input("Input Team 2 Name")
flag1 = False
flag2 = False
score1, score2 = 0,0
moves1, moves2 = [], []
while flag1 == False:
    a = input("Are you done with input for",name1,"? Y/N")
    if a == "Y":
        flag1 = True
        break
    temp = input("Input T(try), C(conversion) or P(penalty kick) for",name1)
    if temp == "T":
        moves1.append("T")
        score1 = score1 + 5
    elif temp == "C":
        moves1.append("C")
        score1 = score1 + 2
    else:
        moves1.append("P")
        score1 = score1 + 3

while flag2 == False:
    a = input("Are you done with input for",name2,"? Y/N")
    if a == "Y":
        flag2 = True
        break
    temp = input("Input T(try), C(conversion) or P(penalty kick) for", name2)
    if temp == "T":
        moves2.append("T")
        score2 = score2 + 5
    elif temp == "C":
        moves2.append("C")
        score2 = score2 + 2
    else:
        moves2.append("P")
        score2 = score2 + 3

print(name1, "scored", score1, "points, through these moves:")
for x in range(len(moves1)):
    print(moves1[x])
print(name2, "scored", score2, "points, through these moves:")
for x in range(len(moves2)):
    print(moves2[x])
