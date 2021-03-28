
numbers = input("Input your numbers with spaces inbetween")
nums = numbers.split()
digits = len(nums)

print(nums)

for x in range(len(nums)):
    if x in range(len(nums)-1):
        if int(nums[x])> int(nums[x+1]):
            temp = nums[x]
            nums[x] = nums[x+1]
            nums[x+1] = temp


print(nums)