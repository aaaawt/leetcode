def majorityElement(nums):
    count = 1
    maj = nums[0]
    for i in range(1, len(nums)):
        if maj == nums[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj = nums[i + 1]
    return maj

print(majorityElement([3, 2, 3]))
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
