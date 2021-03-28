import turtle
turtle.bgcolor("light cyan")
turtle.speed(10)
for i in range(300,-300,-10):
    turtle.penup()
    turtle.goto(-400,i)
    turtle.pendown()
    turtle.forward(600)
turtle.left(90)
for i in range(200,-400,-10):
    turtle.forward(590)
    turtle.penup()
    turtle.goto(i,-290)
    turtle.pendown()