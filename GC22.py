import random

import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

for i in range(1000):
    alex.forward(100)
    alex.left(random.randint(1,360))