def addBinary(a, b):
    return '{:b}'.format(int(a, 2) + int(b, 2))

print(addBinary('11', '1'))
print(addBinary('1010', '1011'))
