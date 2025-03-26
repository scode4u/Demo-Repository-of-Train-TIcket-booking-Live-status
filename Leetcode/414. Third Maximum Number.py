nums = [3,2,1]
nums = list(set(nums))
nums.sort()
if len(nums) < 3:
    print(max(nums))
else:
    print(nums[2])