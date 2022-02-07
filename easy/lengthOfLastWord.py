def lengthOfLastWord(s):
    return len(s.strip().split()[-1])

    # i = -1
    # for i in range(len(s) - 1, -1, -1):
    #     if s[i] != ' ':
    #         break
    # for j in range(i, -1, -1):
    #     if s[j] == ' ':
    #         return i - j
    # return i + 1

print(lengthOfLastWord('Hello World'))
print(lengthOfLastWord('    fly me   to   the moon  '))
print(lengthOfLastWord('luffy is still joyboy'))
print(lengthOfLastWord('l '))