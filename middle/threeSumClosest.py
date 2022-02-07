from bisect import bisect

def threeSumClosest(nums, target):
    if len(nums) == 3:
        return sum(nums)
    nums.sort()
    best_sum = sum(nums[:3])
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            three = target - (nums[i] + nums[j])
            pos = bisect(nums, three, j + 1)
            if pos <= j + 1 or (pos < len(nums) and abs(three - nums[pos]) < abs(three - nums[pos - 1])):
                cur_sum = nums[pos] + nums[i] + nums[j]
            else:
                cur_sum = nums[pos - 1] + nums[i] + nums[j]
            if abs(cur_sum - target) < abs(best_sum - target):
                best_sum = cur_sum
    return best_sum


print(threeSumClosest([-3, -2, -5, 3, -4], -1))
print(threeSumClosest([-1, 2, 1, -4], 1))
print(threeSumClosest([0, 0, 0], 1))