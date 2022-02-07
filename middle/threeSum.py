from bisect import bisect


def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        for j in range(i + 1, len(nums)):
            if nums[i] + 2 * nums[j] > 0:
                break
            pos = bisect(nums, 0 - nums[i] - nums[j], j + 1)
            if pos > j + 1 and nums[pos - 1] == 0 - nums[i] - nums[j]:
                res.append((nums[i], nums[j], 0 - nums[i] - nums[j]))
    return [[x, y, z] for x, y, z in set(res)]


print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([]))
print(threeSum([0]))
