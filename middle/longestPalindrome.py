def longestPalindrome(s):
    res = ' '
    for i in range(len(s)):
        count = s[i]
        r = min(i, len(s) - i - 1)
        for j in range(1, r + 1):
            if s[i - j] == s[i + j]:
                count = s[i - j : i + j + 1]
            else:
                break
        if len(count) >= len(res):
            res = count
    for i in range(len(s)):
        count = s[i]
        r = min(i, len(s) - i - 2)
        for j in range(0, r + 1):
            if s[i - j] == s[i + 1 + j]:
                count = s[i - j : i + j + 2]
            else:
                break
        if len(count) >= len(res):
            res = count
    return res

print(longestPalindrome('aaaa'))
print(longestPalindrome('babad'))
print(longestPalindrome('cbbd'))
print(longestPalindrome('a'))
print(longestPalindrome('ac'))
print(longestPalindrome('bdaca'))