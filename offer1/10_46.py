# 动态规划 Ologn O1
def translateNum(num: int) -> int:
    if num == 0:
        return 1
    s = str(num)
    a = 1
    ans = a
    for i in range(1, len(s)):
        if int(s[i-1]) != 0 and int(s[i-1]+s[i]) <= 25:
            b = ans
            ans += a
            a = b
        else:
            a = ans
    return ans



print(translateNum(12258))
print(translateNum(506))
print(translateNum(18822))
print(translateNum(0))
