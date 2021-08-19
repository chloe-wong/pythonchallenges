def NAND(input1,input2):
    if (input1 == True) and (input2) == True:
        return False
    else:
        return True

def AND(input1,input2):
    a = NAND(input1,input2)
    return(NAND(a,a))

def NOT(input1):
    return(NAND(input1,input1))

def OR(input1,input2):
    a = NAND(input1,input1)
    b = NAND(input2,input2)
    return(NAND(a,b))

def NOR(input1,input2):
    a = OR(input1,input2)
    return(NOT(a))

input1 = input("Input 1")
input2 = input("Input 2")
gate = input("what gate?")
if gate == "NAND":
    print(NAND(input1,input2))
elif gate == "AND":
    print(AND(input1,input2))
elif gate == "NOT":
    print(NOT(input1))
elif gate == "OR":
    print(OR(input1,input2))
elif gate == "NOR":
    print(NOR(input1,input2))