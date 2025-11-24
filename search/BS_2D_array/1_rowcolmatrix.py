a = [[1, 2, 3, 4], 
     [5, 6, 7, 8], 
     [9, 10, 11, 12], 
     [13, 14, 15, 16]]
target = 19

def metrics(nums, target ) :
    r = 0
    c = len(nums)-1
    while(r < len(nums) and c >= 0):

        if nums[r][c] == target:
            res = [r, c]
            return res

        if nums[r][c] > target:
            c -= 1

        if nums[r][c] < target:
            r += 1
    return [-1, -1]

print(metrics(a, target))



