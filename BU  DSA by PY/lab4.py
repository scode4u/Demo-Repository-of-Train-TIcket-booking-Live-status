def mergesort(arr_input, p1, p2, p3):
    arr1 = arr_input[p1:p2]
    arr2 = arr_input[p2:p3+1]
    n1 = len(arr1)
    n2 = len(arr2)
    