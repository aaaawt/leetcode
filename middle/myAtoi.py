def myAtoi(s):
    i = 0
    neg = False
    num = 0
    while i < len(s) and s[i] == ' ':
        i += 1

    if i < len(s):
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            neg = True
            i += 1

    while i < len(s) and ord('0') <= ord(s[i]) <= ord('9'):
        num = num * 10 + (ord(s[i]) - ord('0'))
        i += 1
    if neg:
        num = -num
    if num < -2 ** 31:
        return -2 ** 31
    elif num > 2 ** 31 - 1:
        return 2 ** 31 - 1
    else:
        return num

print(myAtoi('-4-2'))
print(myAtoi('42'))
print(myAtoi('  -42'))
print(myAtoi('4193 with words'))
print(myAtoi('words and 987'))
print(myAtoi('-91283472332'))