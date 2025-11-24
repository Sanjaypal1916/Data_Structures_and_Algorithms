def cyclicSort(arr):
    i = 0
    n = len(arr)
    while(i < n-1):
        if (arr[i] - 1) == i :
            i += 1
        indxcnt = arr[i] - 1
        arr[indxcnt], arr[i] = arr[i],arr[indxcnt] 
    print(arr)
cyclicSort([3,5,2,1,4])
