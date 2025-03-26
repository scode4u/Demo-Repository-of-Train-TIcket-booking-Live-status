class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length1 = len(nums)
        new_nums = set(nums)
        new_nums = list(new_nums)
        for i in range(length1):
            length2 = len(new_nums)
            if length1 == length2:
                return new_nums
            new_nums.append('_')
demo = Solution()
value  = demo.removeDuplicates([1,1,2,3,4])
print(value)


