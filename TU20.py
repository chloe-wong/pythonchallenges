a = []
with open("counter.txt","r") as existing_file:
   for line in existing_file:
      a.append(line.strip('\n'))
start = int(a[-1])+1
with open("counter.txt","a") as existing_file:
   for x in range(start,start+10):
      linetowrite = str(x)+"\n"
      existing_file.write(linetowrite)