import random
floor = int(input("How many floors?"))
floors= []
for x in range(floor):
    floors.append(x+1)
for x in range(len(floors)):
    choice = random.choice(floors)
    print(choice)
    floors.remove(choice)