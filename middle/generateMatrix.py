def generateMatrix(n):
    res = [[0] * n for j in range(n)]
    m = n
    k = 1
    x = 0
    y = -1
    while k <= m ** 2:
        for i in range(x, n):
            res[x][i] = k
            k += 1
        if k > m ** 2:
            break
        for j in range(x + 1, n):
            res[j][n - 1] = k
            k += 1
        if k > m ** 2:
            break
        for i in range(n - 2, y, -1):
            res[n - 1][i] = k
            k += 1
        if k > m ** 2:
            break
        for j in range(n - 2, x, -1):
            res[j][y + 1] = k
            k += 1
        x += 1
        y += 1
        n -= 1
    return res

print(generateMatrix(4))
print(generateMatrix(1))

