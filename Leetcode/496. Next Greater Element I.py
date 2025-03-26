
def nextGreaterElement(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lst = []
        for i in range(len(nums1)):
            for j in range(len(nums2)-1):
                if nums1[i] == nums2[j]:
                    if nums2[j] < nums2[j+1]:
                        lst.append(nums2[j])
        return nums2[j]  

print(nextGreaterElement([4,1,2],[1,3,4,2]))
