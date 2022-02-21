def permuteUnique(nums):
    nums.sort()
    res = []

    def rank(pre, nums):
        n = len(nums)
        if not nums:
            res.append(pre)
            return
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            rank(pre + [nums[i]], nums[:i] + nums[i + 1:])

    rank([], nums)
    return res

print(permuteUnique([1, 1, 2]))
print(permuteUnique([1, 2, 3]))
