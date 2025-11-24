arr = [4,3,2,1,5,6,8,7, 9]
n = len(arr)
i = 0 
while i < n :
    correctidx = arr[i] -1 
    if  correctidx == i :
        i += 1
    elif correctidx != i and correctidx < n  :
        arr[correctidx], arr[i] = arr[i], arr[correctidx]

print(arr)