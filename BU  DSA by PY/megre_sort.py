# def merge_sort(arr):
#     n = len(arr)
#     gap = n // 2
#     while(gap > 0):
#         for i in range(gap, n):
#             j = i 
#             temp = arr[i]
#             while(j >= gap and arr[j-gap] > temp):
#                 arr[j] = arr[j-gap]
#                 j -= gap
#             arr[j] = temp
#         gap = gap // 2
#     return arr

# arr = [21, 3, 8, 6, 19, 12, 2, 5]
# print(merge_sort(arr))