#1
file= open("textfile.txt", "r")
a = []
for line in file:
    a.append(line.strip('\n')
a = reverse(a)
for x in range(len(a)):
    print(a[x])

#2
file= open("textfile.txt", "r")
a = []
for line in file:
    if "snake" in line:
        print(line.strip('\n')

#3
with open("textfile.txt","w") as file:
    x = 1
    for line in file:
        a = []
        a.append(x)
        a.append(line)
        a = " ".join(a)
        file.write(a)
        x = x+1

#4
with open("textfile.txt","w") as file:
    for line in file:
        a = line.split()
        a.pop(0)
        a = " ".join(a)
        file.write(a)
