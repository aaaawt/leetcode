def spiralOrder(matrix):
    m = len(matrix)
    n = len(matrix[0])
    res = []
    k = 0
    x = 0
    y = -1
    while k < len(matrix) * len(matrix[0]):
        for i in range(x, n):
            res.append(matrix[x][i])
        if len(res) >= len(matrix) * len(matrix[0]):
            break
        for j in range(x + 1, m):
            res.append(matrix[j][n - 1])
        if len(res) >= len(matrix) * len(matrix[0]):
            break
        for i in range(n - 2, y, -1):
            res.append(matrix[m - 1][i])
        if len(res) >= len(matrix) * len(matrix[0]):
            break
        for j in range(m - 2, x, -1):
            res.append(matrix[j][y + 1])
        x += 1
        y += 1
        m -= 1
        n -= 1
        k = len(res)
    return res

print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))
print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
