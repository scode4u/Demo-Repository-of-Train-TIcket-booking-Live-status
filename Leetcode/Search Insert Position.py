# class Solution(object):
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         for i in range

# def insert(arr,target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#         else:
#             while (target < arr[i]):
#                 pass
#             else:
#                 arr = list(arr)
#                 arr.append(target)
#         print(arr)

# insert([1,3,4,5,7],6)

# another way 
def insertion(nums, target):
    low = 0
    high = len(nums) - 1