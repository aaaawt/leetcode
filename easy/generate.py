def generate(numRows):
    yh = [[1]]
    for i in range(1, numRows):
        yh.append([1] + [0]*(i - 1) + [1])
        for j in range(1, i):
            yh[i][j] = yh[i - 1][j - 1] + yh[i - 1][j]
    return yh
print(generate(5))
print(generate(1))