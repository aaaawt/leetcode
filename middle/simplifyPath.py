def simplifyPath(path):
    list_path = path.split('/')
    stack = []
    for x in list_path:
        if x == '..':
            if stack:
                stack.pop()
        elif x and x != '.':
            stack.append(x)
    return '/' + '/'.join(stack)

print(simplifyPath('/home/'))
print(simplifyPath('/../'))
print(simplifyPath('/home//foo/'))
print(simplifyPath('/a/./b/../../c/'))
print(simplifyPath('/a/./b/../c/'))
