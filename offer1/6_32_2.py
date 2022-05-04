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
        ans.append([x.val for x in cur])
        cur = []
    return ans
