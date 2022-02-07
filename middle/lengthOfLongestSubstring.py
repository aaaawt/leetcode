def lengthOfLongestSubstring(s):
    if s == '':
        return 0
    ll = []
    res = len(ll)
    for i in range(len(s)):
        try:
            del ll[:ll.index(s[i]) + 1]
        except ValueError:
            pass
        ll.append(s[i])
        res = max(res, len(ll))
    return res

print(lengthOfLongestSubstring("aabaab!bb"))
print(lengthOfLongestSubstring('dvdf'))
print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('bbbbb'))
print(lengthOfLongestSubstring('pwwkew'))
print(lengthOfLongestSubstring(''))