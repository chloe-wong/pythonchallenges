import turtle
no = int(input("how many different x values are there?"))
xvalues = []
yvalues = []
for x in range(no):
    xvalues.append(int(input("input x value")))
    yvalues.append(int(input("input corresponding y value")))
xaxis = int(((no*2)-1)*50)
yaxis = (max(yvalues)*100)+300
turtle.forward(xaxis+50)
turtle.left(180)
turtle.forward(50)
turtle.right(90)
for y in range(no):
    turtle.forward(yvalues[y]*100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(yvalues[y]*100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
turtle.forward(yaxis)