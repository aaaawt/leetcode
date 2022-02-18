def permute(nums):
    res = []

    def rank(pre, nums):
        n = len(nums)
        if not nums:
            res.append(pre)
            return
        for i in range(n):
            rank(pre + [nums[i]], nums[:i] + nums[i+1:])

    rank([], nums)
    return res

print(permute([1, 2, 3]))
print(permute([0, 1]))
print(permute([1]))
