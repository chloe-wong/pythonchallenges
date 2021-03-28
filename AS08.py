from random import randint

x = ["Rock", "Paper", "Scissors"]
computer = x[randint(0,2)]

player = False

while player == False:
    player = input("Rock, Paper, or Scissors?")
    if player == computer:
        print ("Tie!")
    elif player == "Rock":
        if computer == "Paper":
           print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "crushes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "crushes", player)
        else:
            print("You win!", player, "cuts", computer)
    else:
        print("Sorry, that's not a valid play. Check your spelling, and ensure you're using only 'Rock', 'Paper', or 'Scissors!'")
        player = False
        computer = x[randint(0,2)]