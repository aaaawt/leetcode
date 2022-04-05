def removeDuplicates(nums):
    n = len(nums)
    i = 1
    count = 1
    while i < n:
        if nums[i] == nums[i - 1]:
            if count == 2:
                nums.pop(i)
                n -= 1
            else:
                count += 1
                i += 1
        else:
            count = 1
            i += 1
    return n, nums


print(removeDuplicates([1, 1, 1, 2, 2, 3]))
print(removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
