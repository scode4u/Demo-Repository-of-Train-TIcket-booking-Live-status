# num = [1,2,3,5,6]
# hgh =  max(num)
# i = 0
# while (i < hgh):
#     i += 1
#     # print(i)
#     if i not in num:
#         print(i)
#     else:
#         print(hgh+1)

def missingNumber(nums):
    # high = max(nums)
    # i = 0
    # while ( i <= high):
    #     if i not in nums:
    #         return i
    #     elif i in nums:
    #         return high+1
    #     i += 1

    sum = 0
    for i in range(len(nums)):
        sum = sum + nums[i]
    actual_sum = (len(nums) * (len(nums) + 1)) / 2
    return int(actual_sum - sum)




        
        
        # return i + 1
print(missingNumber([3,0,1]))