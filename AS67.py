import random
file = open("pokemon.txt","r")
cards = []
values = []
for line in file:
    cards.append(line.strip('\n'))
for x in range(len(cards)):
    values.append(random.randint(1,100))
player1cards = []
player2cards = []
for x in range(5):
    player1cards.append(random.choice(cards))
    player2cards.append(random.choice(cards))
print("Player 1:",player1cards)
print("Player 2:", player2cards)
p1wins = 0
p2wins = 0
for x in range(5):
    p1choice = int(input("Pick a card,P1"))
    p2choice = int(input("Pick a card,P2"))
    p1card = player1cards[p1choice]
    p2card = player2cards[p1choice]
    player1cards.pop(p1choice)
    player2cards.pop(p2choice)
    p1index = cards.index(p1card)
    p2index = cards.index(p2card)
    p1value = values[p1index]
    p2value = values[p2index]
    if p1value > p2value:
        print("P1 wins this round")
        p1wins = p1wins + 1
    elif p2value > p1value:
        print("P2 wins this round")
        p2wins = p2wins + 1
if p1wins > p2wins:
    print("P1 wins the game")
else:
    print("P2 wins the game")