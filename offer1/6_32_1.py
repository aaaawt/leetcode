import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 时间复杂度On，空间复杂度On
def levelOrder(root: TreeNode) -> List[int]:
    if not root:
        return []
    ans = []
    queue = collections.deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        ans.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return ans
