def isValid(s):
    if len(s) % 2 != 0:
        return False
    ll = []
    for i in s:
        if i == '(' or i == '[' or i == '{':
            ll.append(i)
        elif ll and (i == ')' and ll[len(ll) - 1] == '('
                     or i == ']' and ll[len(ll) - 1] == '['
                     or i == '}' and ll[len(ll) - 1] == '{'):
            ll.pop()
        else:
            return False
    return len(ll) == 0



print(isValid('()'))
print(isValid('()[]{}'))
print(isValid('(]'))
print(isValid('([)]'))
print(isValid('{[]}'))
print(isValid(')}'))
print(isValid('(('))
print(isValid(''))
print(isValid('()}{'))
