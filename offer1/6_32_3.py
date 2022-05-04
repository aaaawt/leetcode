import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrder(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    ans = [[root.val]]
    queue = collections.deque()
    queue.append(root)
    cur = []
    s = 0
    while queue:
        while queue:
            node = queue.popleft()
            if node.left:
                cur.append(node.left)
            if node.right:
                cur.append(node.right)
        if not cur:
            return ans
        queue += cur
        if s % 2 == 0:
            ans.append([x.val for x in cur])
        else:
            item = [x.val for x in cur]
            item.reverse()
            ans.append(item)
        cur = []
        s += 1
    return ans
