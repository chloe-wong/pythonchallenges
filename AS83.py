import turtle
side = int(input())
angle = 180-((180*(side-2))/side)
print(angle)

def printprocedure(side,angle):
    for x in range(side):
        turtle.forward(100)
        turtle.right(angle)
    turtle.forward(200)

for x in range(100):
    printprocedure(side,angle)

turtle.Screen().exitonclick()