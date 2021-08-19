def encrypt(key,message):
    file = open("encoded.txt","w")
    for x in range(len(message)):
        a = message[x].split()
        linearray = []
        result = ""
        for y in range(len(a)):
            b = a[y]
            temparray = []
            for letter in b:
                letter_index = (alpha.find(letter) + key)%len(alpha)
                temparray.append(alpha[letter_index])
            temparray = "".join(temparray)
            linearray.append(temparray)
        linearray.append('\n')
        linearray = " ".join(linearray)
        file.write(linearray)

def decrypt(key,message):
    file = open("decoded.txt","w")
    for x in range(len(message)):
        a = message[x].split()
        linearray = []
        for y in range(len(a)):
            b = a[y]
            temparray = []
            for letter in b:
                letter_index = (alpha.find(letter)-key)%len(alpha)
                temparray.append(alpha[letter_index])
            temparray = "".join(temparray)
            linearray.append(temparray)
        linearray.append('\n')
        linearray = " ".join(linearray)
        file.write(linearray)


choice = int(input("Would you like to decode (0) or encode (1)?"))
message = []
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if choice == 1:
    key = int(input("What key would you like to use for encryption?"))
    file = open("tobeencoded.txt","r")
    for line in file:
        message.append(line.strip('\n'))
    encrypt(key,message)
    answer = open("encoded.txt","r")
    for line in answer:
        print(line.strip('\n'))

elif choice == 0:
    key = int(input("What key would you like to use for decryption?"))
    file = open("tobedecoded.txt","r")
    for line in file:
        message.append(line.strip('\n'))
    decrypt(key,message)
    answer = open("decoded.txt","r")
    for line in answer:
        print(line.strip('\n'))