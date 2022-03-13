def setZeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])
    flag_col0 = any(matrix[i][0] == 0 for i in range(m))
    for i in range(m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    for i in range(m - 1, -1, -1):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        if flag_col0:
            matrix[i][0] = 0
    return matrix

print(setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
