from math import comb


def uniquePaths(m, n):
    return comb(m + n - 2, n - 1)

    # if m == 1 or n == 1:
    #     return 1
    # else:
    #     return uniquePaths(m - 1, n) + uniquePaths(m, n -1)

print(uniquePaths(3, 7))
print(uniquePaths(3, 2))
print(uniquePaths(7, 3))
print(uniquePaths(3, 3))
