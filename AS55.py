import turtle
import random
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.pencolor("white")
seed = []
seednum = []
def MakeSeed():
    num = int(input("What seed do you want to create?"))
    seednum.append(num)
    array = []
    for x in range(1000):
        temp = []
        a = random.randint(-1000,1000)
        b = random.randint(-1000,1000)
        temp.append(a)
        temp.append(b)
        temp = list(map(str,temp))
        temp = " ".join(temp)
        array.append(temp)
    seed.append(array)

MakeSeed()
print(seed)
def RunSeed():
    run = int(input("What seed?"))
    seedtorun = seednum.index(run)
    array = seed[seedtorun]
    for x in range(len(array)):
        temp = array[x].split()
        temp = list(map(int,temp))
        a,b=temp[0],temp[1]
        t.penup()
        t.goto(a,b)
        t.pendown()
        t.dot()
RunSeed()


turtle.Screen().exitonclick()