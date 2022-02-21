def rotate(matrix):
    n = len(matrix) - 1
    for i in range(n):
        for j in range(n, -1, -1):
            matrix + [matrix[j][i]]


print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))
