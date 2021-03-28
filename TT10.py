import turtle
def triangles(x,y,z):
    turtle.speed(0)
    h = z*((3**0.5)/2)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    start = y
    for x in range(30):
        for x in range(30):
            turtle.forward(z)
            turtle.left(120)
            turtle.forward(z)
            turtle.left(120)
            turtle.forward(z)
            turtle.left(120)
            turtle.penup()
            turtle.forward(z)
            turtle.pendown()
        start = start - h
        turtle.penup()
        turtle.goto(x-(30*x),start)
        turtle.pendown()
x = int(input("input starting x coordinate"))
y = int(input("input starting y coordinate"))
z = int(input("input triangle side width"))
triangles(x,y,z)