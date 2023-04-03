f, s, t = float('-inf'), float('-inf'), float('-inf')  
# good think, use and compare in first loop. With None you cant do that
# can be -> and <- or ->> and -> for pointers
###################
nums = [-9,5,6,34]

l = len(nums)     
empty = [[] for x in range(l)]
max = l -1
min = 0
for x in range(l-1, -1, -1):
    if nums[min] ** 2 > nums[max] ** 2:
        empty[x] = nums[min] ** 2
        min += 1
    else:
        empty[x] = nums[max] ** 2
        max -= 1
        
###################
