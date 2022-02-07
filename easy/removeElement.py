def removeElement(nums, val):
    # n = len(nums)
    # i = 0
    # while i < n:
    #     if nums[i] == val:
    #         nums.remove(nums[i])
    #         n -= 1
    #     else:
    #         i += 1
    # return len(nums)

    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index

print(removeElement([3, 2, 2, 3], 3))
print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))