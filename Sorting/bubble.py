# Descending order 
def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] < arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
arr = [4,7,2,9,5,8]
print(bubble_sort(arr))

# Ascending Order

def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
arr = [4,7,2,9,5,8]
print(bubble_sort(arr))

# the Difference between these two program is the sign operator of less  & greater  


# Without Reverse Order 
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
arr = [4,7,2,9,5,8]
print(bubble_sort(arr))
