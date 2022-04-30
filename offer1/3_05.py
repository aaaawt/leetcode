def replaceSpace(s: str) -> str:
    ans = ''
    for x in s:
        if x == ' ':
            x = '%20'
        ans += x
    return ans
