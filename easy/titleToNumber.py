def titleToNumber(columnTitle):
    k = ord('A')
    res = 0
    for i in columnTitle:
        res = res * 26 + (ord(i) - k + 1)
    return res

print(titleToNumber('A'))
print(titleToNumber('AB'))
print(titleToNumber('ZY'))