file = open("C:/Users/chloe/Desktop/words.txt")
con = file.read()
words=con.split(",")
file.close()
letters = ["A","B","C","D","E","F","G","H",'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for x in range(len(words)):
    a = words[x]
    a = a[1:-1]
    words[x] = a
triangles = [ 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120,136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431]
count = 0
def split(z):
    return[char for char in z]
for x in range(len(words)):
    z = words[x]
    zletters = split(z)
    num = 0
    for y in range(len(zletters)):
        a = letters.index(zletters[y])
        num = num + a + 1
    if num in triangles:
        count = count+1
print(count)