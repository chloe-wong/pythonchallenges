questions = []
answers = []
points = 0
q1 = input("User 1, please input your first question")
questions.append(q1)
a1 = input("User 1, please input the answer to your first question")
answers.append(a1)
q1 = input("User 1, please input your second question")
questions.append(q1)
a1 = input("User 1, please input the answer to your second question")
answers.append(a1)
q1 = input("User 1, please input your third question")
questions.append(q1)
a1 = input("User 1, please input the answer to your third question")
answers.append(a1)

print("Pass over to User 2")
print("Question 1:", questions[0])
u2ans = input("Input answer")
if u2ans == answers[0]:
    points = points + 1

print("Question 2:", questions[0])
u2ans = input("Input answer")
if u2ans == answers[1]:
    points = points + 1

print("Question 3:", questions[0])
u2ans = input("Input answer")
if u2ans == answers[2]:
    points = points + 1

print("User 2, you scored:",points,"out of 3")