# # def sorting(arr):
# #     n = len(arr)
# #     for i in range(n-1):
# #         for j in range(i+1,n):
# #             if arr[i] > arr[j]:
# #                 arr[j] , arr[i] = arr[i] , arr[j]   # swapping the number from the first element after comparing with all the others
# #         print(arr)

# # arr = [23,12,67,24,45]
# # sorting(arr)
# # # print(arr)


# # def bubble_sort(arr):
# #     n = len(arr)
# #     for i in range(n-1):
# #         for j in range(0,n-i-1):
# #             if arr[j+1] < arr[j]:
# #                 arr[j+1] , arr[j] = arr[j] , arr[j+1]
# #         print(arr)

# # arr = [23,43,12,56,34]
# # bubble_sort(arr)
# # # print(arr)


# # def insertion_sorting(arr):
# #     n = len(arr)
# #     for i in range(1,n):
# #         item = arr[i]
# #         j = i - 1
# #         while ((arr[j] > item ) and (j >= 0) ):
# #             arr[j+1]=arr[j]
# #             j -= 1
# #         arr[j+1]=item
# #         print(arr)    

# # arr = [12,67,45,89,34]
# # insertion_sorting(arr)



# # Lab 3:
# # merge 

# def merge(arr1, arr2):
#     n1 = len(arr1)
#     n2 = len(arr2)
#     i = 0
#     j = 0
#     k = 0
#     arr = []
#     while ((i<n1) and (j<n2)):
#         if (arr1[i] < arr2[j]):
#             arr.append(arr1[i])
#             i += 1
#             k += 1
#         elif (arr2[j] < arr1[i]):
#             arr.append(arr2[j])
#             j += 1
#             k += 1
#         else:
#             arr.append(arr1[i])
#             i += 1
#             j += 1
#             k += 1
#     while(i<n1):
#         arr.append(arr1[i])
#         i += 1
#         k += 1
#     while(j<n2):
#         arr.append(arr2[j])
#         j += 1
#         k += 1
#         return arr
        
# arr1 = [5,6,12,13]
# arr2 = [1,2,3,7,9,10,15]
# print (merge(arr1, arr2))


# def merging_sort(arr,low,high):
#     if low < high:
#         mid = low+(high-low)//2
#         merging_sort(arr, low , mid)
#         merging_sort(arr, mid+1, high)


def insertion(arr):
    n = len(arr)
    for i in range(n):
        index_item = arr[i]
        last_second = i - 1
        while(arr[last_second] > index_item) and (last_second >= 0):
            arr[last_second+1] = arr[last_second]
            last_second -= 1    
            arr[last_second] = index_item
        print(arr)

arr = [5,9,6,10,14,7]
insertion(arr)