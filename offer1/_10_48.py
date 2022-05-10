# 动态规划+哈希表 On O1
def lengthOfLongestSubstring1(s: str) -> int:
    start = 0
    end = 0
    dic = {}
    for j, x in enumerate(s):
        i = dic.get(x, -1)
        dic[x] = j
        start = start + 1 if start < j - i else j - i
        end = max(end, start)
    return end


# 动态规划+线性遍历 On^2 O1
def lengthOfLongestSubstring2(s):
    end = start = i = 0
    for j, x in enumerate(s):
        i = j - 1
        while i >= 0 and x != s[i]:
            i -= 1
        start = start + 1 if start < j - i else j - i
        end = max(end, start)
    return end


# 双指针+哈希表 On O1
def lengthOfLongestSubstring3(s):
    dic = {}
    end = 0
    i = -1
    for j, x in enumerate(s):
        if x in dic:
            i = max(dic[x], i)
        dic[x] = j
        end = max(end, j-i)
    return end


print(lengthOfLongestSubstring1("abcabcbb"))
print(lengthOfLongestSubstring1("bbbbb"))
print(lengthOfLongestSubstring1("pwwkew"))
