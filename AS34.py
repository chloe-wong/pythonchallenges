import turtle
import random

def tree(branchLen,t):
    if branchLen > 5:
        t.pensize(((branchLen)/2)-5)
        t.forward(branchLen)
        t.right(random.randint(15,20))
        tree(branchLen-15,t)
        t.left(random.randint(15,20))
        tree(branchLen-15,t)
        t.right(random.randint(15,20))
        t.backward(branchLen)
    if branchLen == 15:
        t.color("green")
    if branchLen > 15:
        t.color("brown")

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(random.randint(15, 20))
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    tree(75,t)
    myWin.exitonclick()

main()