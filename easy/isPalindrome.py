def isPalindrome(s):
    s = s.lower()
    i = 0
    j = -1
    while i < j + len(s):
        if s[i].isalnum() and s[j].isalnum() and s[i] == s[j]:
            i += 1
            j -= 1
        if s[i].isalnum() and s[j].isalnum() and s[i] != s[j]:
            return False
        if not s[i].isalnum():
            i += 1
        if not s[j].isalnum():
            j -= 1
    return True

print(isPalindrome('A man, a plan, a canal: Panama'))
print(isPalindrome('race a car'))
print(isPalindrome(' '))