import random
uppers = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special = ['!','@','#','$','%','^','&','*']
randomarray = []
uppernum = random.randint(1,6)
lowernum = random.randint(1,6)
specialnum = random.randint(1,6)
for x in range(uppernum):
    randomarray.append(random.choice(uppers))
for x in range(lowernum):
    randomarray.append(random.choice(lowers))
for x in range(specialnum):
    randomarray.append(random.choice(special))
random.shuffle(randomarray)
password = "".join(randomarray)


flag = False
while True:
    if flag == True:
        print("password is:", trypassword)
        break
    else:
        testerarray = []
        puppernum = random.randint(1, 6)
        plowernum = random.randint(1, 6)
        pspecialnum = random.randint(1, 6)
        for x in range(puppernum):
            testerarray.append(random.choice(uppers))
        for x in range(plowernum):
            testerarray.append(random.choice(lowers))
        for x in range(pspecialnum):
            testerarray.append(random.choice(special))
        random.shuffle(testerarray)
        trypassword = "".join(testerarray)
        print(trypassword)
        if trypassword == password:
            flag = True