
# // https://leetcode.com/problems/missing-number/
# // Amazon Question

arr = [1,4,3,2,5, 6, 8,9]
i = 0 
n = len(arr)

while i < n :
    correctidx = arr[i] -1 
    if correctidx != i and correctidx < n :
        arr[correctidx], arr[i] = arr[i], arr[correctidx]
    else : 
        i += 1

for i in range(n):
    correctidx = arr[i] -1 
    if correctidx != i :
        print(i+1)

print(arr)
