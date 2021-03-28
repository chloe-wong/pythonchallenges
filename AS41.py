a = int(input("even or odd parity? even = 0, odd = 1"))
b = input("input 7 bits of data")
p = int(input("what should the parity bit be?"))
temp = []
def split(b):
    return[char for char in b]
x = split(b)
y = x.count("1")
if a == 0:
    if y%2 == 0:
        parity = 0
    else:
        parity = 1
else:
    if y%2 == 0:
        parity = 1
    else:
        parity = 0
if p == parity:
    print("correct")
else:
    print("wrong")

temp.append(parity)
temp.append(b)
temp = list(map(str,temp))
print("the answer is parity bit:",parity)
print("the byte is:", "".join(temp))