def searchInSorted(arr, k):
    if k in arr:
        return True
    return False

print(searchInSorted([1, 2, 3, 4, 6], 6))