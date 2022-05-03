from typing import List


# 时间复杂度O(nm)
def findNumberIn2DArray1(matrix: List[List[int]], target: int) -> bool:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return True
    return False

# 时间复杂度O(n+m)
def findNumberIn2DArray2(matrix: List[List[int]], target: int) -> bool:
    if not matrix:
        return False
    upper = len(matrix)
    row = 0
    col = len(matrix[0]) - 1
    while row < upper and col >= 0:
        if target == matrix[row][col]:
            return True
        elif target < matrix[row][col]:
            col -= 1
        else:
            row += 1
    return False

print(findNumberIn2DArray2([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30],[20,27,30,36,40]], 20))
