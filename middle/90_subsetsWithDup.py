def subsetswithdup(nums):
    ans = []
    pre = []

    def dfs(pre, num):
        ans.append(list(pre))
        if len(num) == 0:
            return
        for i in range(len(num)):
            if i > 0 and num[i] == num[i-1]:
                continue
            pre.append(num[i])
            dfs(pre, num[i+1:])
            pre.pop()

    nums.sort()
    dfs(pre, nums)
    return ans


print(subsetswithdup([1, 2, 2]))
print(subsetswithdup([0]))
