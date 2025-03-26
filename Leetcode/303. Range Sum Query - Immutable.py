
# brutforce code 

# from typing import List
# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.name = nums



#     def sumRange(self, left: int, right: int) -> int:
#         newList  = (self.nums[left:right+1])
#         sum = 0
#         for i in newList:
#             sum = sum + i
#         return sum

        


# # Your NumArray object will be instantiated and called as such:
# obj = NumArray(-2, 0, 3, -5, 2, -1)
# param_1 = obj.sumRange(left,right)



# Optimized code 

from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        current = 0
        for i in nums:
            current += i
            self.prefix.append(current)


    def sumRange(self, left: int, right: int) -> int:
        right = self.prefix[right]
        left = self.prefix[left - 1] if left > 0 else 0
        return right - left