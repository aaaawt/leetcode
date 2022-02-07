x = eval(input('x = '))
t = x
y = 0
# y = x[::-1]
# print(x == y)
if x < 0:
    print(False)
while x != 0:
    y = y * 10 + x % 10
    x = x // 10
print(t == y)