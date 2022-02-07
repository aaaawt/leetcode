def strStr(haystack, needle):
    if needle == '':
        return 0
    for i in range(len(haystack)-len(needle) + 1):
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                break
        else:
            return i
    return -1

    # if needle == '':
    #     return 0
    # n = len(needle)
    # i = 0
    # while i < len(haystack):
    #     if haystack[i:i + n] == needle:
    #         return i
    #     i += 1
    # return -1

    # if needle == '':
    #     return 0
    # for i in range(len(haystack)-len(needle) + 1):
    #     nmatch = False
    #     for j in range(len(needle)):
    #         if haystack[i+j] != needle[j]:
    #             nmatch = True
    #             break
    #     if not nmatch:
    #         return i
    # return -1

print(strStr('a', 'a'))
print(strStr('hello', 'll'))
print(strStr('aaaaa', 'bba'))
print(strStr('', ''))
print(strStr('mississippi', 'issipi'))
print(strStr('bab', 'bb'))