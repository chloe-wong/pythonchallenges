#1
response = [10, 8, 6, 4, 2]
1) if start < stop, step > 0
2) if start > stop, step < 0

#2
two turtle instances: alex is an unlinked copy of tess.
Adjusting alex's color thus does not affect tess's color

#3
before:
a = [1,2,3]
b = [1,2,3]

after:
a = [1,2,3]
b = [5,2,3]

#4
The first test will output False.
The second test will output True

#5
def add_vectors(u,v):
    temp = []
    for x in range(len(u)):
        a = u[x] + v[x]
        temp.append(a)
    print(temp)

#6
def scalar_mult(s,v):
    temp = []
    for x in range(len(v)):
        a = s*v[x]
        temp.append(a)
    print(temp)

#7
def dot_product:
        temp = []
    for x in range(len(u)):
        a = u[x]*v[x]
        temp.append(a)
    print(sum(temp))

#9
def replace(s,old,new):
    a=s.replace(old,new)
    print(a)
replace("Mississippi","i","I")
