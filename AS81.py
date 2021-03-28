list = [1,2,3,4,5]
def sumproduct(list):
    print(sum(list))
    product = 1
    for x in range(len(list)):
        product = product*list[x]
    print(product)