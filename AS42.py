p1health = 100
p2health = 100
moves = ["punch","kick","regain health","trip","stab"]
damage = [-5,-10,+10,-2,-20]
while True:
    if p1health <= 0:
        print("P2 Wins")
        break
    elif p2health <= 0:
        print("P1 Wins")
        break
    p1move = input("P1 input your move")
    p2move = input("P2 input your move")
    move1index = moves.index(p1move)
    move2index = moves.index(p2move)
    p1health = p1health + damage[move1index]
    p2health = p2health + damage[move2index]