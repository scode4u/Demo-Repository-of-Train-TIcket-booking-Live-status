def insertion(arr):
    for i in range(1, len(arr)):
        j = i
        while ( arr[j-1] > arr[j]) and j > 0:
            arr[j-1] , arr[j] = arr[j] , arr[j-1]
            j -= 1

arr = [5,3,7,9,2,1]
insertion(arr)
print(arr)
