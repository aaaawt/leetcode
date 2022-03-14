def searchMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    start = 0
    end = rows * cols - 1
    while start <= end:
        mid = (start + end) // 2
        m = mid // cols
        n = mid % cols
        if matrix[m][n] > target:
            end = mid - 1
        elif matrix[m][n] < target:
            start = mid + 1
        else:
            return True
    return False

print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 7))
print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 61))
