choice = int(input("Decode (0) or encode (1)?"))
morse = ["._","_...","_._.","_..",".",".._.","__.","....","..",".___","_._.","._..","__","_.","___",".__.","__._","._.","...","_",".._","..._",".__","_.._","_.__","__..",".____","..___","...__","...._",".....","_....","__...","___..","____.","_____"]
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]
def split(word):
    return[char for char in word]
def DecodeMorse(string):
    a = string.split("   ")
    translatedfull = []
    for x in range(len(a)):
        b = a[x]
        word = b.split()
        temparray = []
        for y in range(len(word)):
            c = word[y]
            found = morse.index(c)
            translate = letters[found]
            temparray.append(translate)
        temparray = "".join(temparray)
        translatedfull.append(temparray)
    return(translatedfull)

def EncodeMorse(string):
    a = string.split(" ")
    translatedfull = []
    for x in range(len(a)):
        b = a[x]
        word = split(b)
        temparray = []
        for y in range(len(word)):
            c = word[y]
            found = letters.index(c)
            translate = morse[found]
            temparray.append(translate)
        temparray = " ".join(temparray)
        translatedfull.append(temparray)
    return(translatedfull)

if choice == 0:
    string = input("Input Morse to decode")
    print("Your decoded text is:"," ".join(DecodeMorse(string)))
elif choice == 1:
    string = input("Input text to encode")
    print("Your encoded text is:","   ".join(EncodeMorse(string)))