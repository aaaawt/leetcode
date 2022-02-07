def searchInsert(nums, target):
    l = 0
    h = len(nums)
    while h - l != 0:
        k = (h + l) // 2
        if target > nums[k]:
            l = k + 1
        elif target < nums[k]:
            h = k
        else:
            return k
    return l

    # i = 0
    # while i < len(nums) and nums[i] < target:
    #     i += 1
    # return i

print(searchInsert([1, 3, 5, 6], 5))
print(searchInsert([1, 3, 5, 6], 2))
print(searchInsert([1, 3, 5, 6], 7))
print(searchInsert([1, 3, 5, 6], 0))
print(searchInsert([1], 0))