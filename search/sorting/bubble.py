arr = [5,6,7,3,2,1,4,7,8,9,10]

for i in range(len(arr)):
    for j in range(1, len(arr)-i):
        if arr[j]<arr[j-1]:                # either start with j = 1 and add compare j-1
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp

# OR
n = len(arr)
for i in range(n):
    for j in range(n-i-1):
        if arr[j] > arr[j+1] :          # or start with j =0 and compare with j+1
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp 


print(arr)