arr = [16, 17, 4, 3, 5, 2]
arr.reverse()
max_one = arr[0]
new = []
new.append(max_one)

for i in range(len(arr)):
    min = i
    for j in range(i+1,len(arr)):
        if arr[min] < arr[j]:
            
            min = j
print(new)

# def s(arr):
#     for i in range(len(arr)):
#         minimum_pos = i
#         for j in range(i , len(arr)):
#             if arr[j] < arr[minimum_pos]:
#                 minimum_pos= j
#         temp = arr[i]
#         arr[i] = arr[minimum_pos]
#         arr[minimum_pos] = temp
#     return arr

# arr = [12,45,23,78,56]
# print(s(arr))