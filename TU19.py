with open("counter.txt", "w") as new_file:
   for i in range(10, -1, -1):
      linetowrite = str(i)+"\n"
      new_file.write(linetowrite)
with open("counter.txt","r") as new_file:
   for line in new_file:
      print(line,end="")