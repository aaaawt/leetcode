# 两次遍历字符串，时间复杂度On，空间复杂度O|Omiga|
import collections


def firstUniqChar1(s: str) -> str:
    count = {}
    for ch in s:
        if ch not in count:
            count[ch] = 1
        else:
            count[ch] += 1
    for ch in s:
        if count[ch] == 1:
            return ch
    return ' '

# 一次遍历字符串，一次遍历哈希表，时间复杂度On，空间复杂度O|Omiga|
def firstUniqChar2(s: str) -> str:
    count = {}
    for i, ch in enumerate(s):
        if ch in count:
            count[ch] = -1
        else:
            count[ch] = i
    n = len(s)
    for x in count.values():
        if x != -1:
            n = min(x, n)
    return ' ' if n == len(s) else s[n]


# 遍历一遍字符串，运用哈希表与队列，时间复杂度On，空间复杂度O|Omiga|
def firstUniqChar3(s: str) -> str:
    count = {}
    q = collections.deque()
    n = len(s)
    for i, ch in enumerate(s):
        if ch not in count:
            count[ch] = i
            q.append((s[i], i))
        else:
            count[ch] = -1
            while q and count[q[0][0]] == -1:
                q.popleft()
    return ' ' if not q else q[0][0]
