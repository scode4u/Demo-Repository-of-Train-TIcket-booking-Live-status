arr = [2,1,3,4]
n = len(arr)
# if len(arr) <= 1:
#     print(True)
# else:
#     for i in range(1,n):                      # by me
#         if arr[i-1] > arr[i]:
#             arr[i-1] , arr[i] = arr[i] , arr[i-1]
count = 0
# for i in range(len(arr)):
#     if ( arr[i] > arr[(i+1) % len(arr)]):       # by youtube
#         count += 1
# print(count <= 1)

for i in range(len(arr)):
    if arr[i-1] > arr[i]:      # by me 
        count += 1
print(count <= 1)