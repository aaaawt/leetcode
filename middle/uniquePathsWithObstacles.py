def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [0] * n

    dp[0] = int(obstacleGrid[0][0] == 0)

    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[j] = 0
            elif obstacleGrid[i][j] == 0 and j - 1 >= 0:
                dp[j] += dp[j-1]
    return dp[-1]

print(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(uniquePathsWithObstacles([[0]]))
