w = int(input("type in width(pixels)"))
h = int(input("type in height(pixels)"))
bd = int(input("type in bit depth"))
x = w*h*bd
by = round(x/8/1024/1024,2)
print("One image takes",by,"MB")