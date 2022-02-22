def myPow(x, n):
    s = 1.0
    if n == 0:
        return 1.0
    elif n < 0:
        x = 1 / x
        n = -n
    i = n
    while i > 0:
        if i % 2 != 0:
            s *= x
        x *= x
        i //= 2
    return s

print(myPow(2.00000, 10))
print(myPow(2.10000, 3))
print(myPow(2.00000, -2))
