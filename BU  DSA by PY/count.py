def count(arr):
    max1 = max(arr)
    arr1 = [0]*(max1 + 1)
    arr2 = []
    for i  in range(len(arr)):
        arr1[arr[i]] += 1
    print(arr1)
    for i in range(len(arr1)):
        for _ in range(arr1[i]):
            arr2.append(i)

    return arr2
print(count([1,2,2,1,4,3,1,4,3,2]))