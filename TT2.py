import turtle
write = input("input text")
words = write.split()
print(words)
for x in range(len(words)):
    k = len(words[x])
    turtle.write(words[x])
    turtle.forward(k*4)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()

