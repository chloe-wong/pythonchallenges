import turtle

minimum = int(input("Input Minimum"))
maximum = int(input("Input Maximum"))
upper = int(input("Input Upper Quartile"))
lower = int(input("Input Lower Quartile"))
median = int(input("Input Median"))
mintolower = lower-minimum
lowertomed = median-lower
medtoupper = upper-median
uppertomax = maximum-upper
t = turtle.Turtle()
t.left(90)
t.forward(100)
t.left(180)
t.forward(50)
t.left(90)
t.forward(mintolower*3)
t.left(90)
t.forward(50)
t.left(180)
t.forward(100)
t.left(180)
t.forward(50)
t.right(90)
t.forward(lowertomed*3)
t.left(90)
t.forward(50)
t.left(180)
t.forward(100)
t.left(180)
t.forward(50)
t.right(90)
t.forward(medtoupper*3)
t.left(90)
t.forward(50)
t.left(180)
t.forward(100)
t.left(180)
t.forward(50)
t.right(90)
t.forward(uppertomax*3)
t.left(90)
t.forward(50)
t.left(180)
t.forward(100)
t.left(180)
t.forward(50)
t.right(90)
t.right(180)
t.forward(uppertomax*3)
t.right(90)
t.forward(50)
t.left(90)
t.forward((upper-lower)*3)
t.left(90)
t.forward(100)
t.left(90)
t.forward((upper-lower)*3)

turtle.Screen().exitonclick()