def encrypt(text,s):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result+= chr((ord(char) + s-65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

text = str(input("What is your text?"))
s = int(input("Input Key"))
print("Original Text:", text)
print("Key:", s)
print ("Encoded:", encrypt(text,s))