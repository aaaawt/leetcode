def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    res = [[20001] * (n+1) for i in range(m+1)]
    res[0][1] = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            res[i][j] = grid[i-1][j-1] + min(res[i-1][j], res[i][j-1])
    return res[-1][-1]

print(minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(minPathSum([[1, 2, 3], [4, 5, 6]]))
