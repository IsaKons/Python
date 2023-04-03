#Лист содержит значения в 1-длинна листа. Нужно вывести недостающие для полгоно покрытия значений
nums = [1, 2, 3, 3, 4, 5, 6, 7, 7]
for n in nums:
    print("#########")
    print(nums)
    a = abs(n) - 1
    print(a)
    if nums[a] > 0: nums[a] *= -1
    print(nums[a])
    print("**********")
print([i+1 for i in range(len(nums)) if nums[i] > 0])