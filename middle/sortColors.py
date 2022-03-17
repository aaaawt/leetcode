def sortColors(nums):
    n = len(nums) - 1
    m = 0
    for i in range(n+1):
        while i <= n and nums[i] == 2:
            nums[i], nums[n] = nums[n], nums[i]
            n -= 1
        if nums[i] == 0:
            nums[i], nums[m] = nums[m], nums[i]
            m += 1
    return nums

print(sortColors([2, 0, 2, 1, 1, 0]))
print(sortColors([2, 0, 1]))
print(sortColors([2, 1, 2]))
print(sortColors([1, 2, 0, 0]))