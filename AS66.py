#Four-in-a-row Challenge - www.101computing.net/four-in-a-row-challenge/
import turtle
from random import randint
from time import sleep
YELLOW=1
RED=2

#Draw the grid on screen with all the tokens
def drawGrid(grid):
  global RED, YELLOW
  #Clear the screen
  #myPen.clear()
  myPen.setheading(0)
  myPen.goto(-150,130)
  for row in range (0,6):
      for col in range (0,7):
    		if grid[row][col]==0:
    		  myPen.fillcolor("#FFFFFF")
    		elif grid[row][col]==RED:
    		  myPen.fillcolor("#FF0000")
    		elif grid[row][col]==YELLOW:
    		  myPen.fillcolor("#FFFF00")
		
    		myPen.begin_fill()
    		myPen.circle(25)
    		myPen.end_fill()
	
    		myPen.penup()
    		myPen.forward(50)
    		myPen.pendown()	
      myPen.setheading(270)
      myPen.penup()
      myPen.forward(50)
      myPen.setheading(180)
      myPen.forward(50*7)
      myPen.setheading(0)
      myPen.getscreen().update()

def checkIfWinner(grid, color):
  a = checklines(grid,color)
  b = checkdiags(grid,color)
  if a == True:
    return color
  elif b == True:
    return color
  elif b == True and a == True:
    return color
  else:
    return 0

def checklines(self, marker):
  for line in self:
    for x in range(0,len(line)):
      if x < len(line) - 3:
        if line[x] == line[x+1] == line[x+2] == line[x+3] == " "+marker:
          return True

def checkDiags(self, marker):
  diagBoard = []
  for i, line in enumerate(self.board):
    for idx, item in enumerate(line):
                # Find of there is some marker
      if item == ' ' + marker:
        diagBoard.append(int(str(i)+str(idx)))

  for item in diagBoard:
    if int(item) + 11 in diagBoard and int(item) + 22 in diagBoard and int(item) + 33 in diagBoard:
        return True

  for item in reversed(diagBoard):
    if int(item) - 9 in diagBoard and int(item) - 18 in diagBoard and int(item) - 27 in diagBoard:
        return True



#Main Program Starts Here
myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(500)
window = turtle.Screen()
window.bgcolor("#2288FF")
myPen.color("#2288FF")
myPen.tracer(0)
myPen.speed(0)

#Initialise empty 6 by 7 connect4 grid
connect4=[]
for row in range(0,6):
  connect4.append([])
  for col in range(0,7):
    connect4[row].append(0)

#Play the game, take it in turn. Up to 42 turns
for turn in range(1,43):
  #Randomly pick an column that is not full
  column = randint(0,6)
  while connect4[0][column]!=0:
    #This column is already full, pick another one
    column = randint(0,6)

  #Make the token slide to the bottom of the grid (Stacked on top of any other existing tokens)
  row=5
  while connect4[row][column]!=0:
    row=row - 1

  #Find out the colour of the current player (1 or 2)
  playerColor = (turn % 2) + 1
  #Place the token on the grid
  connect4[row][column]=playerColor
  #Draw the grid
  drawGrid(connect4)

  #Check if this token wins the game
  winner = checkIfWinner(connect4, playerColor)
  if winner==RED:
    myPen.penup()
    myPen.color("#FF0000")
    myPen.goto(-70, -170)
    myPen.write("RED Wins!", None, None, "24pt bold")
    myPen.getscreen().update()
    break  #Stop the game
  elif winner==YELLOW:
    myPen.penup()
    myPen.color("#FFFF00")
    myPen.goto(-80, -170)
    myPen.write("Yellow Wins!", None, None, "24pt bold")
    myPen.getscreen().update()
    break  #Stop the game

  sleep(0.2)