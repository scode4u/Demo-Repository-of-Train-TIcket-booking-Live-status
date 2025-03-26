# Ascending Order

def selection_sort(arr):
    for i in range(len(arr)):
        minpose = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minpose]:
                minpose = j
        temp_variable = arr[i]
        arr[i] = arr[minpose]
        arr[minpose] = temp_variable
    return arr

arr = [3,9,6,2,8,1]
print(selection_sort(arr))

# Descending Order

def selection_sort(arr):
    for i in range(len(arr)):
        minpose = i
        for j in range(i, len(arr)):
            if arr[j] > arr[minpose]:
                minpose = j
        temp_variable = arr[i]
        arr[i] = arr[minpose]
        arr[minpose] = temp_variable
    return arr

arr = [3,9,6,2,8,1]
print(selection_sort(arr))
