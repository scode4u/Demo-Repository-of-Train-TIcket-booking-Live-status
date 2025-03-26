# Minimum steps to sort the array using bubble sort 

arr = [1,4,3,2,5,7,6,9,8,0]
swaps = 0

for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
        if len(arr) == 0: # if is used to check the condition wether it strue or not 
            print("[]")
        elif arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swaps += 1

print("Sorted array:", arr)
print("Minimum steps:", swaps)



def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1

nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  
