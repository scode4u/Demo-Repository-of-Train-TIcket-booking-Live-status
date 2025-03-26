nums = [2,2,1]
nums.sort()
for i in range(len(nums)):
    if nums.count(nums[i]) > 1:
        pass
    else:
        print(nums[i])
