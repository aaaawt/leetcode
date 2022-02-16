def combinationSum2(candidates, target):
    candidates.sort()
    res = []

    def combination(pre, candidates, target):
        if target == 0:
            res.append(pre)
            return
        if not candidates:
            return
        x = candidates[0]
        if x > target:
            return
        combination(pre + [x], candidates[1:], target - x)
        for i in range(1, len(candidates)):
            if candidates[i] != candidates[i - 1]:
                combination(pre, candidates[i:], target)
                break

    combination([], candidates, target)
    return res

print(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(combinationSum2([2, 5, 2, 1, 2], 5))
