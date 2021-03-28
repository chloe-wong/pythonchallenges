def split(text):
    return[char for char in text]

text = input("Input your text")
letters = split(text)
lets = len(letters)
a = lets-1
answer = []
for x in range(lets):
    answer.append(letters[a])
    a = a-1

print(''.join(answer))