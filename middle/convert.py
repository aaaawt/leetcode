def convert(s, numRows):
    if numRows == 1:
        return s
    n = numRows * 2 - 2
    ll = [''] * numRows
    for i, x in enumerate(s):
        stat = i % n
        ll[stat if stat < numRows else numRows - stat - 2] += x
    return ''.join(ll)

print(convert('PAYPALISHIRING', 3))
print(convert('PAYPALISHIRING', 4))
print(convert('A', 1))