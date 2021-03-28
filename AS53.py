votes = [["Alice","Bob","Charlie"],
         ["Alice","Bob","Charlie"],
         ["Bob","Alice","Charlie"],
         ["Bob","Alice","Charlie"],
         ["Bob","Alice","Charlie"],
         ["Charlie","Alice","Bob"],
         ["Charlie","Alice","Bob"],
         ["Charlie","Bob","Alice"],
         ["Charlie","Bob","Alice"]]

winner = False
winnername = ""
while True:
    if winner == True:
        print("The winner is:",winnername)
        break
    else:
        alicecount = 0
        bobcount = 0
        charliecount = 0
        for x in range(len(votes)):
            a = votes[x][0]
            if a == "Alice":
                alicecount = alicecount + 1
            elif a == "Bob":
                bobcount = bobcount + 1
            elif a == "Charlie":
                charliecount = charliecount + 1
        if alicecount > (len(votes)/2):
            winner = True
            winnername = "Alice"
        elif bobcount > (len(votes)/2):
            winner = True
            winnername = "Bob"
        elif charliecount > (len(votes)/2):
            winner = True
            winnername = "Charlie"
        else:
            if (charliecount < bobcount < alicecount) or (charliecount < alicecount < bobcount):
                for x in range(len(votes)):
                    votes[x].remove("Charlie")
            elif (bobcount < charliecount < alicecount) or (bobcount < alicecount < charliecount):
                for x in range(len(votes)):
                    votes[x].remove("Bob")
            elif (alicecount < bobcount < charliecount) or (alicecount < charliecount < bobcount):
                for x in range(len(votes)):
                    votes[x].remove("Alice")
