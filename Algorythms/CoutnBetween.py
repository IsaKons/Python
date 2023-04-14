# Find shortest distance what contains sum of elems = target.
target = 7
nums = [2, 3, 1, 2, 4, 3]
if len(nums) == 0:
    resultant = 0
start, end = 0, 0
dist, summa = float("inf"), nums[0]
while end <= len(nums) - 1:
    if summa < target:
        end += 1
        if end <= len(nums) - 1:
            summa += nums[end]
    elif summa >= target:
        dist = min(end - start + 1, dist)
        summa -= nums[start]
        start += 1
resultant = dist if dist != float("inf") else 0
