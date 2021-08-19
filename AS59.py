board = [[0,0,0],
         [0,0,0],
         [0,0,0]]
winner = False
winnername = ""
while True:
    if winner == True:
        print("winner is",winnername)
        break
    else:
        player1row = int(input("Input Player 1 Move Row"))
        player1column = int(input("Input Player 1 Move Column"))
        board[player1row][player1column] = "X"
        if (board[0][0] == "X") and (board[0][1] == "X") and (board[0][2] == "X"):
            winner = True
            winnername = "P1"
        elif (board[0][0] == "X") and (board[1][0] == "X") and (board[2][0] == "X"):
            winner = True
            winnername = "P1"
        elif (board[0][0] == "X") and (board[1][1] == "X") and (board[2][2] == "X"):
            winner = True
            winnername = "P1"
        elif (board[0][1] == "X") and (board[1][1] == "X") and (board[2][1] == "X"):
            winner = True
            winnername = "P1"
        elif (board[1][0] == "X") and (board[1][1] == "X") and (board[1][2] == "X"):
            winner = True
            winnername = "P1"
        elif (board[0][2] == "X") and (board[1][2] == "X") and (board[2][2] == "X"):
            winner = True
            winnername = "P1"
        elif (board[0][2] == "X") and (board[1][1] == "X") and (board[2][0] == "X"):
            winner = True
            winnername = "P1"
        elif (board[2][0] == "X") and (board[2][1] == "X") and (board[2][2] == "X"):
            winner = True
            winnername = "P1"
        else:
            player2row = int(input("Input Player 2 Move Row"))
            player2column = int(input("Input Player 2 Move Column"))
            board[player2row][player2column] = "O"
            if (board[0][0] == "O") and (board[0][1] == "O") and (board[0][2] == "O"):
                winner = True
                winnername = "P2"
            elif (board[0][0] == "O") and (board[1][0] == "O") and (board[2][0] == "O"):
                winner = True
                winnername = "P2"
            elif (board[0][0] == "O") and (board[1][1] == "O") and (board[2][2] == "O"):
                winner = True
                winnername = "P2"
            elif (board[0][1] == "O") and (board[1][1] == "O") and (board[2][1] == "O"):
                winner = True
                winnername = "P2"
            elif (board[1][0] == "O") and (board[1][1] == "O") and (board[1][2] == "O"):
                winner = True
                winnername = "P2"
            elif (board[0][2] == "O") and (board[1][2] == "O") and (board[2][2] == "O"):
                winner = True
                winnername = "P2"
            elif (board[0][2] == "O") and (board[1][1] == "O") and (board[2][0] == "O"):
                winner = True
                winnername = "P2"
            elif (board[2][0] == "O") and (board[2][1] == "O") and (board[2][2] == "O"):
                winner = True
                winnername = "P2"