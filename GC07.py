balance = 1000
n = int(input("How much would you like to withdraw?"))
if n%5== 0:
    if n<=1000:
        balance = balance-(0.5+n)
        print("Your balance is", balance)
    else:
        print("You have insufficient funds.")
else:
    print("Your withdrawal amount must be a multiple of 5.")

