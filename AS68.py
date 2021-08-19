import random
deck = ["Blue 0","Red 0","Yellow 0","Green 0"]
player1hand = []
player2hand = []

def CreateDeck():
    for x in range(1,10):
        temp = ["Blue"]
        temp.append(str(x))
        temp = " ".join(temp)
        deck.append(temp)
        deck.append(temp)

        temp = ["Green"]
        temp.append(str(x))
        temp = " ".join(temp)
        deck.append(temp)
        deck.append(temp)

        temp = ["Red"]
        temp.append(str(x))
        temp = " ".join(temp)
        deck.append(temp)
        deck.append(temp)

        temp = ["Yellow"]
        temp.append(str(x))
        temp = " ".join(temp)
        deck.append(temp)
        deck.append(temp)

    for x in range(2):
        deck.append("Blue Draw Two")
        deck.append("Green Draw Two")
        deck.append("Red Draw Two")
        deck.append("Yellow Draw Two")

    for x in range(2):
        deck.append("Blue Reverse")
        deck.append("Green Reverse")
        deck.append("Red Reverse")
        deck.append("Yellow Reverse")

    for x in range(4):
        deck.append("Wild Card")
        deck.append("Wild Draw Four")

def DealCards():
    for x in range(7):
        a = random.choice(deck)
        deck.remove(a)
        player1hand.append(a)
        b = random.choice(deck)
        deck.remove(b)
        player2hand.append(b)
    print(player1hand)
    print(player2hand)

CreateDeck()
DealCards()
random.shuffle(deck)

topcard = deck[0]

while True:
    if len(player1hand) == 0:
        print("Player 1 wins")
        break
    elif len(player2hand)==0:
        print("Player 2 wins")
        break
    else:
        print(topcard)
        print("Player 1 Turn")
        choice = int(input("Would you like to play(0) or draw(1)?"))
        if choice == 0:
            topcard = input("Input the card you would like to play")
            player1hand.remove(topcard)
            deck.insert(0,topcard)
            b = topcard.split()
            if (b[0] == "Wild") and (b[1] == "Draw"):
                for x in range(4):
                    draw = deck[-1]
                    deck.remove(draw)
                    player2hand.append(draw)
            elif (b[1] == "Draw"):
                for x in range(2):
                    draw = deck[-1]
                    deck.remove(draw)
                    player2hand.append(draw)
        else:
            draw = deck[-1]
            deck.remove(draw)
            player1hand.append(draw)

        print(topcard)
        print("Player 2 Turn")
        choice = int(input("Would you like to play(0) or draw(1)?"))
        if choice == 0:
            topcard = input("Input the card you would like to play")
            player2hand.remove(topcard)
            deck.insert(0, topcard)
            b = topcard.split()
            if (b[0] == "Wild") and (b[1] == "Draw"):
                for x in range(4):
                    draw = deck[-1]
                    deck.remove(draw)
                    player1hand.append(draw)
            elif (b[1] == "Draw"):
                for x in range(2):
                    draw = deck[-1]
                    deck.remove(draw)
                    player1hand.append(draw)

        else:
            draw = deck[-1]
            deck.remove(draw)
            player2hand.append(draw)