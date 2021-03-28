#task1
array = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
number = int(input())
print(array[number])
---
#task2
start = int(input("what is your starting day number?"))
stay = int(input("what is the length of your stay?"))
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
mod = ((stay+start)%7)
print (days[mod])
---
#task6

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,49.9, 45, 44.9, 40, 39.9, 2, 0]
answers = []
for x in range(len(xs)):
    if xs[x]<40:
        answers.append("F3")
    elif xs[x]>=40 and xs[x]<45:
        answers.append("F2")
    elif xs[x]>=45 and xs[x]< 50:
        answers.append("F1 Supp")
    elif xs[x]>=50 and xs[x]< 60:
        answers.append("Third")
    elif xs[x]>=60 and xs[x]< 70:
        answers.append("Second")
    elif xs[x]>=70 and xs[x]< 75:
        answers.append("Upper Second")
    else:
        answers.append("First")

for x in range(len(xs)):
    print (xs[x])
    print (answers[x])
---
