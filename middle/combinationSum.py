def combinationSum(candidates, target):
    candidates.sort()
    ans = []

    def combination(pre, candidates, target):
        if target == 0:
            ans.append(pre)
            return
        if not candidates:
            return
        x = candidates[0]
        n = target // x
        for i in range(n, -1, -1):
            combination(pre + [x] * i, candidates[1:], target - x * i)

    combination([], candidates, target)
    return ans

print(combinationSum([2, 3, 6, 7], 7))
print(combinationSum([2, 3, 5], 8))
print(combinationSum([2], 1))
