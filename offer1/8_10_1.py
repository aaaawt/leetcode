# 动态规划 On O1
def fib1(n: int):
    mod = 10 ** 9 + 7
    if n < 2:
        return n
    p, q, r = 0, 0, 1
    for i in range(2, n + 1):
        p = q
        q = r
        r = (p + q) % mod
    return r

# 快速幂算法 Ologn O1
def fib(n: int) -> int:
    mod = 10 ** 9 + 7
    if n < 2:
        return n

    def multiply(a, b):
        c = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                c[i][j] = (a[i][0] * b[0][j] + a[i][1] * b[1][j]) % mod
        return c

    def matrix_pow(a, n):
        ret = [[1, 0], [0, 1]]
        while n > 0:
            if n & 1:  # 把n转换为二进制，当n末尾为1时为真
                ret = multiply(ret, a)
            n >>= 1  # 右移，右移一位相当于除以2
            a = multiply(a, a)
        return ret

    res = matrix_pow([[1, 1], [1, 0]], n - 1)
    return res[0][0]
