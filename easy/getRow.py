def getRow(rowindex):
    cur = 1
    res = []
    for i in range(rowindex + 1):
        res.append(cur)
        cur = cur * (rowindex - i) // (i + 1)
    return res

print(getRow(3))
print(getRow(0))
print(getRow(1))