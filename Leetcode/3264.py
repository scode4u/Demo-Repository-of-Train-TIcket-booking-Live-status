class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        for i in range(k):
            minval = min(nums)
            index = nums.index(minval)
            nums[index] = nums[index] * multiplier 
        return nums
    
demo = Solution()
val = demo.getFinalState([2,1,3,4,5],3,4)
print(val)