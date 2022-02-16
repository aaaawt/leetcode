def multiply(num1, num2):
    if num1 == '0' or num2 == '0':
        return '0'
    if len(num1) < len(num2):
        num1, num2 = num2, num1

    def add(n1, n2):
        i = len(n1) - 1
        j = len(n2) - 1
        ans = ''
        k = 0
        while i >= 0 or j >= 0:
            a = ord(n1[i]) - ord('0') if i >= 0 else 0
            b = ord(n2[j]) - ord('0') if j >= 0 else 0
            n = a + b + k
            ans = str(n % 10) + ans
            k = n // 10
            i -= 1
            j -= 1
        if k:
            ans = str(k) + ans
        return ans

    i = len(num1) - 1
    j = len(num2) - 1
    res = ''
    ans = ''
    k = 0
    while j >= 0 and i >= 0:
        a = ord(num1[i]) - ord('0')
        b = ord(num2[j]) - ord('0')
        n = a * b + k
        ans = str(n % 10) + ans
        k = n // 10
        i -= 1
        if i == -1:
            if k:
                ans = str(k) + ans
            j -= 1
            i = len(num1) - 1
            ans = ans + '0' * (len(num2) - 2 - j)
            res = add(ans, res)
            ans = ''
            k = 0
    return res

print(multiply('999', '999'))
print(multiply('123', '456'))
