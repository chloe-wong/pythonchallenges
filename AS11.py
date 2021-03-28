import random
upper,lower = list(map(chr, range(65, 91))),list(map(chr, range(97, 123)))
special = ["!","#","$","^","&","*","^"]
number = ['1','2','3','4','5','6','7','8','9','0']
no = [3,4,5,6,7]
lowerno, upperno, specialno = random.choice(no), random.choice(no), random.choice(no)
uppers = random.sample(upper,upperno)
lowers = random.sample(lower,lowerno)
specials = random.sample(special, specialno)
numbers = random.sample(number,specialno)
chars = []
for x in range(len(uppers)):
    chars.append(uppers[x])
for x in range(len(lowers)):
    chars.append(lowers[x])
for x in range(len(specials)):
    chars.append(specials[x])
for x in range(len(numbers)):
    chars.append(numbers[x])
y = len(chars)
chars = random.sample(chars,y)
print("".join(chars))