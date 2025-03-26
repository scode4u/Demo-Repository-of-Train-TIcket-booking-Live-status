# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
nums1 = [1,2,2,1]
nums2 = [2,2]
new = []
for i in range(nums1):
    if nums1[i] in nums2:
        new.append(nums1[i])
print(new)
