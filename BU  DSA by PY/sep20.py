import numpy as np
import time
import random
from matplotlib import pyplot as plt

def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

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

arr = [12,43,456,86,34,13,89,52,34]

t_selection = []
t_bubble = []

for i in range(1001,10001,50):
    arr = np.random.randint(1,100,i)
    t1 = time.time()
    bubble_sort(arr)
    t2 = time.time()
    t_b = t2 - t1
    # print(t_s)
    t1 = time.time()
    selection_sort(arr)
    t2 = time.time()
    t_s = t2 - t1
    t_selection.append(t_s)
    t_bubble.append(t_b)

x = np.arange(1,11,1)
plt.plot(x,t_selection)
plt.plot(x,t_bubble)
plt.show()

def fib(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)
    
print(fib(23))