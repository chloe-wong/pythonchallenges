isbn = input("Input the ISBN number")
def split(n):
    return [char for char in n]
n = isbn.split()
nums = split(n[1])
givencheck = nums[9]
if givencheck != "X":
    givencheck = int(givencheck)
nums.pop(9)
nums = list(map(int, nums))
multipliers = [10, 9, 8, 7, 6, 5, 4, 3, 2]
result = [nums[i]*multipliers[i] for i in range(len(multipliers))]
a = sum(result)
print(a)
remainder = a%11
remainder = 11-remainder
if remainder == 11:
    calcheck = 0
elif remainder == 10:
    calcheck = "X"
else:
    calcheck = remainder
print(calcheck)
if calcheck == givencheck:
    print("correct entry")
else:
    print("incorrect entry")