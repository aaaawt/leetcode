s = input('s = ')
keys = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
values = [1, 5, 10, 50, 100, 500, 1000]
dd = dict(zip(keys, values))
x = 0
i = 0
while i < len(s):
    a = dd[s[i]]
    b = dd[s[i + 1]] if i < len(s) - 1 else 0
    if a >= b:
        x += a
        i += 1
    else:
        x += b - a
        i += 2
print(x)