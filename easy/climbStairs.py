def climbStairs(n):
    res = [1, 2]
    for i in range(2, n + 1):
        res.append(res[i - 1] + res[i - 2])
    return res[n - 1]

print(climbStairs(2))
print(climbStairs(3))
print(climbStairs(22))