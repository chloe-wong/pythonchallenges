#exercise1
import time
file1= open("rudyard.txt", "r")
for line in file1:
    print(line,end="")
    time.sleep(2.5)

#exercise2

import time
file1= open("rudyard.txt", "r")
file2 = open("mam.txt","r")
x = int(input("Would you like the version with male (0) or female (1) pronouns?"))
if x == 0:
   for line in file1:
      print(line,end="")
      time.sleep(2.5)
elif x == 1:
   for line in file2:
      print(line,end="")
      time.sleep(2.5)