import time
x = int(input("how many seconds would you like?"))
for y in range(x,0,-1):
    print(y)
    time.sleep(1)
print("Blast off!")