nums =  [4,3,2,7,8,2,3,1]
n = []
nums = set(nums)
for i in range(1,len(nums)+1):
    if (i not in nums):
        n.append(i)
print(n)
