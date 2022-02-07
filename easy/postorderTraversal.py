from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root: Optional[TreeNode]):
    if not root:
        return []
    tree = []
    tree.extend(postorderTraversal(root.left))
    tree.extend(postorderTraversal(root.right))
    tree.append(root.val)
    return tree

print(postorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))))
print(postorderTraversal(None))
print(postorderTraversal(TreeNode(1)))