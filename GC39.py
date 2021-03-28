import random
name = input("input student name")
insults = [", you're the reason the gene pool needs a lifeguard",
           ", if i had a face like yours, I'd sue my parents",
           ", you must have been born on a highway cos' that's where the most accidents happen",
           ", if laughter is the best medicine, your face must be curing the world",
           ", I'd agree with you but then we'd both be wrong",
           ", if I had a dollar for every time you said something smart, I'd be broke",
           ", I'll never forget the first time we met. But I'll keep trying!",
           ", you're entitled to your incorrect opinion",
           ", whoever told you to be yourself gave you really bad advice",
           ", where's your off button?",
           ", I'm jealous of people who don't know you",
           ", you sound reasonable right now...time to up my medication"]

a = random.choice(insults)
print(name+a)
