def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = (m+n)-1
    for l in range(m+n):
        while(j >=0):
            if (i>=0 and nums1[i] > nums2[j]):
                nums1[k] = nums1[i]
                # k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1       
            k -= 1
    return nums1    
print(merge([1,2,3,0,0,0],3,[2,5,6],3))






    # for j in range(n):
    #     nums1[m+j] = nums2[j]
    #     nums1.sort()