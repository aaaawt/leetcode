def removeDuplicates(nums):
    # n = len(nums)
    # i = 0
    # while i < n:
    #     j = i + 1
    #     while j < n:
    #         if nums[i] != nums[j]:
    #             break
    #         else:
    #             nums.remove(nums[j])
    #             n -= 1
    #             j -= 1
    #         j += 1
    #     i += 1
    # return len(nums), nums
    index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[index] = nums[i]
            index += 1
    return index, nums

print(removeDuplicates([1, 1, 2]))
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))