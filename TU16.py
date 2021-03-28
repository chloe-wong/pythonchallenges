#exercise1
ringgit = 129.0
print(f"RM{int(ringgit)}")

#exercise2
numcol1 = [4.12313,9.392432,10.9344,6.3453490]
numcol2 = [3.304293,5.943058,9.493584903,9.23904]
numcol3 = [4.390482,6.23904832,7.329048,1.190238]
headers = ["row 1:", "row 2:", "row 3:", "row 4:"]

for x in range(len(numcol1)):
    print(f"{headers[x]} {numcol1[x]:^15.3f} {numcol2[x]:^15.2f} {numcol3[x]:^15.2f}")


#exercise3
x = int(input("Please input a value to convert to binary"))
print(f"{x} in binary is {bin(x)}")