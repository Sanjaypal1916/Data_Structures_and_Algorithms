import math

arr = [5,6,7,3,2,1,4,11,7,8,9]
n=len(arr)


def findmaxidx(arr, endIdx):
    max_idx = 0
    for i in range(1, endIdx):
        if arr[max_idx] < arr[i]:
            max_idx = i
    return max_idx 

print(findmaxidx(arr, n))

for i in range(n):
    max = findmaxidx(arr, n-i)
    arr[n-i-1], arr[max] = arr[max], arr[n-i-1]

print(arr)
    



