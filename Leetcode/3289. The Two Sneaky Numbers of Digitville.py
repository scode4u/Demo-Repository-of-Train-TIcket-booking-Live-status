# def getSneakyNumbers(nums):
#     n = len(nums)
#     res = []
#     for i in range(n):
#         if nums.count(nums[i]) >= 2:
#             res.append(nums[i])
#         res = list(set(res))
#     return res
# print(getSneakyNumbers([0,1,1,0]))




# User function Template for python3

def lenOfLongestSubarr(arr, k):  
    cumulative_sum = 0
    max_len = 0
    sum_index_map = {0: -1}  # Base case for subarrays starting at index 0

    for i in range(len(arr)):
        cumulative_sum += arr[i]

        # Check if there's a subarray that sums to k
        if cumulative_sum - k in sum_index_map:
            max_len = max(max_len, i - sum_index_map[cumulative_sum - k])

        # Record the first occurrence of the cumulative sum
        if cumulative_sum not in sum_index_map:
            sum_index_map[cumulative_sum] = i

    return max_len

print(lenOfLongestSubarr([6,4,2,1,9],13))
