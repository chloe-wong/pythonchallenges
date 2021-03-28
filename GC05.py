#sequence
print("you have to do things in order")
print("like this")
print("otherwise everything")
print("will not work or make sense!")


#selection
print("first, you pick something: you make a choice")
choice = int(input("input either 1 or 2"))
print("different things happen depending on your choice")
if choice == 1:
    print("you chose one, huh?")
elif choice == 2:
    print("guess you chose two.")

#repetition
print("you're going to do something many, many times. Iteration!")
choice = int(input("how many times do you want to see your name?"))
name = input("wait, what is your name again?")
for x in range(choice):
    print(name)

#variable
print("variables store different things, like numbers or strings")
number = 22
name = "Sally"
boolean = True
date = 13/09/2020
print(number)
print(name)
print(boolean)
print(date)