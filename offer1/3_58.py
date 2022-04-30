def reverseLeftWords1(s: str, n: int) -> str:
    return s[n:] + s[:n]

def reverseLeftWords2(s: str, n: int) -> str:
    left = ''
    ans = ''
    for i, x in enumerate(s):
        if i < n:
            left += x
        else:
            ans += x
    return ans + left

def reverseLeftWords3(s: str, n: int) -> str:
    res = ''
    for i in range(n, n+len(s)):
        res += s[i % len(s)]
    return res
