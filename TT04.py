import turtle
j = int(input("please enter the number of sides"))
a = (180*(j - 2))/j
print(a)
for x in range(j):
    turtle.forward(50)
    turtle.right(180 - a)