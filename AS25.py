
stars = input("Please input your integers with a space in between")
star_list = stars.split()

for x in range(len(star_list)):
    temp = []
    for y in range(int(star_list[x])):
        temp.append("*")
    print(''.join(temp))
