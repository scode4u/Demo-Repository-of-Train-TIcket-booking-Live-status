nums = [1,0,1,1]
k = 1
st_idx = []
for i in range(len(nums)):
    if 2 <= nums.count(nums[i]):
        st_idx.append(i)
print(st_idx)
if len(st_idx) >= 3:
    if (len(st_idx)-1) - st_idx[0] <= k :
        print(True)
    else:
        print(False)
else:
    if len(st_idx) - st_idx[0] <= k:
        print(True)
    else:
        print(False)


        # Y chat gpt 
def containsNearbyDuplicate(nums, k):
    index_map = {}  # To store the last seen index of each number
    
    for i, num in enumerate(nums):
        if num in index_map and i - index_map[num] <= k:
            return True
        index_map[num] = i  # Update the index of the current number
    
    return False
print(containsNearbyDuplicate([1,0,1,1],3))