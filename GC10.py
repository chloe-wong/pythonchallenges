nterms = (int(input("How many terms would you like printed?")))

n1 = 0
n2 = 1
count = 0

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print(nterms, "terms of the Fibonacci Sequence.")
    print(n1)
else:
    print(nterms, "terms of the Fibonacci Sequence.")
    while count < nterms:
        print(n1, end = ',')
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1