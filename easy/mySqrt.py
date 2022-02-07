def mySqrt(x):
    m = x / 2
    while abs(m ** 2 - x) > 0.1:
        m = m / 2 + x / (2 * m)
        print(m)
    return int(m)

print(mySqrt(0))
print(mySqrt(1))
print(mySqrt(121))
print(mySqrt(40000))
print(mySqrt(81))

