arr = [5,6,7,3,2,1,4,7,8,9,10]
n = len(arr)

for i in range(n-1):
    for j in range(i+1, 0, -1):
        if arr[j] < arr[j-1]:
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp

print(arr)

    

    