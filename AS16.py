#exercise 1
import turtle
for x in range(5):
    for y in range(4):
        turtle.forward(20)
        turtle.left(90)
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()

#exercise 2
import turtle

for x in range(4):
    turtle.forward(20)
    turtle.left(90)
turtle.penup()
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(10)
turtle.right(180)
turtle.pendown()
for x in range(4):
    turtle.forward(40)
    turtle.left(90)
turtle.penup()
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(10)
turtle.right(180)
turtle.pendown()
for x in range(4):
    turtle.forward(60)
    turtle.left(90)
turtle.penup()
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(10)
turtle.right(180)
turtle.pendown()
for x in range(4):
    turtle.forward(80)
    turtle.left(90)
turtle.penup()
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(10)
turtle.right(180)
turtle.pendown()
for x in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.penup()
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(10)
turtle.right(180)
turtle.pendown()

#exercise 3
import turtle
def draw_poly(n, sz):
    angle = 180-(((n-2)*(180))/n)
    for x in range(n):
        turtle.forward(sz)
        turtle.left(angle)
draw_poly(8,50)

#exercise 4
import turtle
turtle.speed(0)
for x in range(5):
    for x in range(4):
        turtle.forward(50)
        turtle.right(90)
    turtle.left(90)
    for x in range(4):
        turtle.forward(50)
        turtle.right(90)
    turtle.left(90)
    for x in range(4):
        turtle.forward(50)
        turtle.right(90)
    turtle.left(90)
    for x in range(4):
        turtle.forward(50)
        turtle.right(90)
    turtle.left(90)
    turtle.right(18)

#exercise 6
import turtle
def draw_poly(n, sz):
    angle = 180-(((n-2)*(180))/n)
    for x in range(n):
        turtle.forward(sz)
        turtle.left(angle)

def draw_equitriangle(t, sz):
    draw_poly(t, sz)

draw_equitriangle(3,50)

#exercise 9
import turtle
def draw_star():
    for x in range(5):
        turtle.left(144)
        turtle.forward(100)
draw_star()

#exercise 10
import turtle
def draw_star():
    for x in range(5):
        for x in range(5):
            turtle.left(144)
            turtle.forward(100)
        turtle.penup()
        turtle.forward(350)
        turtle.right(144)
        turtle.pendown()
draw_star()