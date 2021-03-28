url = "C:\\Users\\chloe\\Desktop\\practice.txt"
file = open(url, 'r')
words = 0
chars = 0
for line in file:
    line = line.strip("\n")
    word = line.split()
    words += len(word)
    chars += len(line)
file.close()
print(chars/words)