def convertToTitle(columnNumber):
    k = ord('A')
    s = ''
    while columnNumber != 0:
        columnNumber -= 1
        s = chr(columnNumber % 26 + k) + s
        columnNumber //= 26
    return s

print(convertToTitle(1))
print(convertToTitle(28))
print(convertToTitle(701))
print(convertToTitle(2147483647))