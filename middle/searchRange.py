def searchRange(nums, target):
    if not nums:
        return [-1, -1]
    l = 0
    n = len(nums) - 1
    while l != n:
        m = (l + n) // 2
        if nums[m] >= target:
            n = m
        else:
            l = m + 1
    if nums[n] != target:
        return [-1, -1]
    left = l
    l = 0
    n = len(nums)
    while l != n:
        m = (l + n) // 2
        if nums[m] > target:
            n = m
        else:
            l = m + 1
    return [left, l - 1]

print(searchRange([1], 0))
print(searchRange([5, 5], 5))
print(searchRange([5, 8, 8, 8, 8, 10], 8))
print(searchRange([5, 5, 8, 8, 8, 10], 5))
print(searchRange([5, 7, 7, 8, 8, 10], 6))
print(searchRange([], 0))
