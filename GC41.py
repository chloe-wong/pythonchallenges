n = int(input("What number would you like to check?"))
while n > 2:
    if n%3 == 0:
        print (n, "is a multiple of 3")
        break
    else:
        print(n, "is not a multiple of 3")
        break