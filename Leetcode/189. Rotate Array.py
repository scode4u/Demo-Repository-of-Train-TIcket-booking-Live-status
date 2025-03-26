arr =  [1,2]
k = 3
# for i in range(k):
#     arr[i] , arr[i+1] = arr[i+1] , arr[i]  # done by me 
#     print(arr)

if len(arr) < k:
    # k -= 1
    # arr = arr.reverse()
    arr[:] = reversed(arr[:])
    print(arr)
else:
    arr.reverse()
    arr[:k] = reversed(arr[:k])
    #                               Done by chat gpt 
    arr[k:] = reversed(arr[k:])
    print(arr)

