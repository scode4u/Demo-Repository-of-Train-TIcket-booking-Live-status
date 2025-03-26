def dup(arr,s):
    n = len(arr)
    s = set()
    for i in range(n):
        if arr[i] in s:
            return True
        else:
            s.add(arr[i])
    
    return False
print(dup([1,2,3,1],()))