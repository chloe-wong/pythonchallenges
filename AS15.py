MyList = [1,2,3,4,5]
def listsum(numList):
    if len(numList)==1:
        return numList [0]
    else:
        return numList[0] + listsum(numList[1:])

print (listsum([1,2,3,4,5]))