def graycode(n):
    return [i ^ i >> 1 for i in range(2 ** n)]


print(graycode(2))
print(graycode(1))
print(graycode(3))
