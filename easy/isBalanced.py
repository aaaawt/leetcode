from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root: TreeNode):
    def recursion(node: TreeNode) -> Optional[int]:
        """return None if unbalanced, else the depth of the subtree"""
        if not node:
            return 0
        left = recursion(node.left)
        if left is None:
            return None
        right = recursion(node.right)
        if right is None:
            return None
        if abs(left - right) <= 1:
            return max(left, right) + 1
        return None
    return recursion(root) is not None


print(isBalanced(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
print(isBalanced(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))))
print(isBalanced(TreeNode()))