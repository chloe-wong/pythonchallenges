import pandas as pd
import random2 as rand
df = pd.read_excel(r'C:\Users\chloe\Downloads\words.xls')
mylist = df['Word'].tolist()
def split(word):
	return[char for char in word]
word = split(rand.choice(mylist))
chances = 10
spaces = []
for x in range(len(word)):
	spaces.append("_")
while True:
	if chances == 0:
		print("game over")
		print("the word was:", word)
		break
	elif "_" not in spaces:
		print("good job! The word is:",word)
		break
	else:
		print(spaces)
		letter = input("Guess a letter")
		print(chances)
		if letter in word:
			temp = word.index(letter)
			spaces[temp] = letter
			print(spaces)
		else:
			chances = chances - 1