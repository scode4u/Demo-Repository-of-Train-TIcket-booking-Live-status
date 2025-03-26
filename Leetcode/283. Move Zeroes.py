nums = [0,1,0,3,12]
# count = 0
for i in range(len(nums)):
    if nums[i] == 0:
        # count += 1
        nums.append(nums[i]) 
        nums.remove(nums[i])
print(nums)
