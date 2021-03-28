import random
choice = ["confess", "stay silent"]
compdec = (random.choice(choice))
playchoice = str(input("Do you wish to stay silent or confess?"))

if compdec == playchoice == 'stay silent':
    print ("You are both in prison for a year")

if compdec == playchoice == 'confess':
    print("You are both in prison for five years")

if compdec == 'stay silent' and playchoice == 'confess':
    print("You are released from prison. Your partner stayed silent and is incarcerated for twenty years.")

if compdec == 'confess' and playchoice == 'stay silent':
    print("You are in prison for twenty years. Your partner confessed and was released.")

q = str(input("Would you like to try again? Yes or No?"))

if q == 'Yes' or 'yes':
    compdec = (random.choice(choice))
    playchoice = str(input("Do you wish to stay silent or confess?"))

    if compdec == playchoice == 'stay silent':
        print ("You are both in prison for a year")

    if compdec == playchoice == 'confess':
        print("You are both in prison for five years")

    if compdec == 'stay silent' and playchoice == 'confess':
        print("You are released from prison. Your partner stayed silent and is incarcerated for twenty years.")

    if compdec == 'confess' and playchoice == 'stay silent':
        print("You are in prison for twenty years. Your partner confessed and was released.")







