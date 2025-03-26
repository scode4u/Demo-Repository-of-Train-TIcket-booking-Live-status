# def merge(arr):
#     if len(arr) > 1:

#         left_arr = arr[:len(arr)//2]
#         right_arr = arr[len(arr)//2:]

#         merge(left_arr)
#         merge(right_arr)

#         i , j , k = 0, 0, 0

#         while i < len(left_arr) and j < len(right_arr):
#             if left_arr [i] < right_arr[j]:
#                 arr[k] = left_arr[i]
#                 i += 1
#             else:
#                 arr[k] = right_arr[j]
#                 j += 1
#                 k += 1

#         while i < len(left_arr):
#             arr[k] = left_arr[i]
#             i += 1
#             k += 1

#         while j < len(right_arr):
#             arr[k] = right_arr[j]
#             j += 1
#             k += 1

# arr  = [2,4,1,3,8,6,7,9,5,12,45,23,67,13]
# merge(arr)
# print(arr)




# # def merge_sort(arr):
# #     if len(arr) > 1:

# #         left_arr = arr[:len(arr)//2]
# #         right_arr = arr[len(arr)//2:]

# #         merge_sort(left_arr)
# #         merge_sort(right_arr)

# #         i = 0
# #         j = 0
# #         k = 0

# #         while i < len(left_arr) and j < len(right_arr):
# #             if left_arr[i] < right_arr[j]:
# #                 arr[k] = left_arr[i]
# #                 i += 1
# #             else:
# #                 arr[k] = right_arr[j]
# #                 j += 1
# #             k += 1

# #         while i < len(left_arr):
# #             arr[k] = left_arr[i]
# #             i += 1
# #             k += 1
        
# #         while j < len(right_arr):
# #             arr[k] = right_arr[j]
# #             j += 1
# #             k += 1

# # arr  = [12,45,34,89,67,54,19]
# # merge_sort(arr)
# # print(arr)




def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # merge(left, right)

    return merge(left, right)

def merge(left, right):
    ressult = []
    while(len(left) > 0 and len(right) > 0):
        if left[0] < right[0]:
            ressult.append(left.pop(0))
        else:
            ressult.append(right.pop(0))
    ressult.extend(left)
    ressult.extend(right)
    return ressult

arr = [12,45,23,67,55]
print(merge_sort(arr))