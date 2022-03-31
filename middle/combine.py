def combine(n, k):
    ans = []

    def sub_combine(m, k):
        res.append(m)
        if k == 1:
            ans.append(res.copy())
            res.pop()
            return
        for j in range(m + 1, n + 1):
            sub_combine(j, k - 1)
        res.pop()

    res = []
    for i in range(1, n + 1):
        sub_combine(i, k)
    return ans

print(combine(4, 2))
print(combine(5, 3))
print(combine(1, 1))