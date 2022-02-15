def countAndSay(n):
    if n == 1:
        return '1'
    s = countAndSay(n - 1)
    i = 0
    count = 1
    res = ''
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            i += 1
            count += 1
        else:
            res += str(count) + s[i]
            i += 1
            count = 1
    res += str(count) + s[-1]
    return res

print(countAndSay(1))
print(countAndSay(4))