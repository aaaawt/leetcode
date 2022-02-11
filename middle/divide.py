def divide(dividend, divisor):
    if divisor == 1:
        return dividend
    if divisor == -1:
        if dividend == -2147483648:
            return 2147483647
        return -dividend
    negden = False
    negsor = False
    if dividend < 0 and divisor < 0:
        negden = True
        dividend = abs(dividend)
        negsor = True
        divisor = abs(divisor)
    elif dividend < 0 and divisor > 0:
        negden = True
        dividend = abs(dividend)
    elif dividend > 0 and divisor < 0:
        negsor = True
        divisor = abs(divisor)
    mul = [divisor, ]
    ans = [1, ]
    s = divisor
    t = 1
    while s < dividend:
        s += s
        t += t
        mul.append(s)
        ans.append(t)
    res = 0
    for i in range(len(mul) - 1, -1, -1):
        if dividend >= mul[i]:
            dividend -= mul[i]
            res += ans[i]
    if negden and not negsor or negsor and not negden:
        res = -res
    return res

print(divide(-2147483648, 2))
print(divide(10, 3))
print(divide(7, -3))
