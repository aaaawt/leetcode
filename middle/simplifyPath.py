def simplifyPath(path):
    list_path = path.split('/')
    stack = []
    for x in list_path:
        if x == '' or x == '.':
            continue
        elif x == '..':
            if stack:
                stack.pop()
        else:
            stack.append(x)
    return '/' + '/'.join(stack)

print(simplifyPath('/home/'))
print(simplifyPath('/../'))
print(simplifyPath('/home//foo/'))
print(simplifyPath('/a/./b/../../c/'))
print(simplifyPath('/a/./b/../c/'))
