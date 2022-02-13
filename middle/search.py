def search(nums, target):
    l = 0
    h = len(nums)
    while l != h:
        m = (l + h) // 2
        if nums[m] == target:
            return m
        elif nums[m] > nums[0]:
            if nums[0] <= target < nums[m]:
                h = m
            else:
                l = m + 1
        else:
            if nums[m] < target <= nums[h - 1]:
                l = m + 1
            else:
                h = m
    return -1


    # for i in range(len(nums)):
    #     if nums[i] == target:
    #         return i
    # return -1

print(search([4, 5, 6, 7, 0, 1, 2], 3))
print(search([4, 5, 6, 7, 1, 2, 3], 3))
print(search([4, 5, 6, 7, 1, 2, 3], 4))
print(search([4, 5, 6, 7, 1, 2, 3], 5))
print(search([1], 0))
