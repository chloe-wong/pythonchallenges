import random
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
substitution = [x for x in alphabet]
random.shuffle(substitution)
message = input("Input your message in all caps")
print("Your initial message is:",message)
message = message.split()
encoded = []
for x in range(len(message)):
    a = message[x]
    temparray = []
    for letter in a:
        letterindex = alphabet.index(letter)
        newalphabet = substitution[letterindex]
        temparray.append(newalphabet)
    temparray = "".join(temparray)
    encoded.append(temparray)
print("The substitution is:",substitution)
encoded = " ".join(encoded)
print("Your coded message is:",encoded)