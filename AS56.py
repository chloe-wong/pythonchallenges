import random

def twos(val_str,bytes):
    import sys
    val = int(val_str,2)
    b = val.to_bytes(bytes,byteorder = sys.byteorder,signed=False)
    return int.from_bytes(b,byteorder=sys.byteorder,signed = True)
def getBit(y,x):
    return str((x>>y)&1)
def tobin(x,count=8):
    shift = range(count-1,-1,-1)
    bits = map(lambda y: getBit(y,x),shift)
    return "".join(bits)

temparray = []
type = int(input("Dec-->Bin(0) or Bin-->Dec(1)"))
if type == 0:
    num = int(input("Maximum?"))
    num2 = int(input("Minimum?"))
    question = random.randint(num2,num)
    print("Convert",question,"to binary")
    answer = tobin(question)
    useranswer = int(input("input your answer"))
    if answer == useranswer:
        print("correct")
    else:
        print("incorrect")

elif type == 1:
    num = int(input("How many digits?"))
    for x in range(num):
        temparray.append(random.randint(0,1))
    temparray = list(map(str,temparray))
    question = "".join(temparray)
    print("Convert",question,"to decimal")
    answer = twos(question,1)
    useranswer = int(input("input your answer"))
    if answer == useranswer:
        print("correct")
    else:
        print("incorrect")