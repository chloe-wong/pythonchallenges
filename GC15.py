for i in range(6):
    for a1 in range((6-i)):
        print(" ", end="")
    for a2 in range(i):
        print(a2+1, "", end="")
    print()
for i in range(6, -1, -1):
    for a1 in range((6-i)):
        print(" ", end="")
    for a2 in range(i):
        print(a2+1, "", end="")
    print()