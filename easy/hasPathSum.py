from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: Optional[TreeNode], targetSum: int):
    if not root:
        return False
    if not root.left and not root.right and root.val == targetSum:
        return True
    return hasPathSum(root.left, targetSum-root.val) or hasPathSum(root.right, targetSum-root.val)

print(hasPathSum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))), 22))
print(hasPathSum(TreeNode(1, TreeNode(2), TreeNode(3)), 5))
print(hasPathSum(None, 0))