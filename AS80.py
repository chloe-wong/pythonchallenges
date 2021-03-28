import math
r = float(input("Input radius"))
def cal_area(r):
    return(1/2*r*r*math.pi)
def cal_circ(r):
    return(2*r*math.pi)
a = cal_area(r)
c = cal_circ(r)
print("the area is", round(a,1))
print("the circumference is", round(c,1))