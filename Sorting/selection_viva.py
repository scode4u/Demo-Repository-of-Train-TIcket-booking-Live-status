def s(arr):
    for i in range(len(arr)):
        minimum_pos = i
        for j in range(i , len(arr)):
            if arr[j] < arr[minimum_pos]:
                minimum_pos= j
        temp = arr[i]
        arr[i] = arr[minimum_pos]
        arr[minimum_pos] = temp
    return arr

arr = [12,45,23,78,56]
print(s(arr))


