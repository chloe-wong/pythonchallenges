import time

hr = float(input("How many hours until the rocket must set off?"))
s = hr*60*60

print("There are", s, "seconds until the rocket must set off. Timer starting now.")

while s>=0:
    print(s)
    s = s-1
    time.sleep(1)

print("ROCKET SET OFFFFFF!!!!!")
