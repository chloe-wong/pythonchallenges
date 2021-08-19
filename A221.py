def remove_duplicates():
    global s
    s = set(s)
    s = list(s)
    return(s)

listy = input("input list values, space separated")
s = listy.split()
print(remove_duplicates())