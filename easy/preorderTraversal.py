from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root: Optional[TreeNode]):
    if not root:
        return []
    tree = []
    tree.append(root.val)
    tree.extend(preorderTraversal(root.left))
    tree.extend(preorderTraversal(root.right))
    return tree

print(preorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))))
print(preorderTraversal(None))
print(preorderTraversal(TreeNode(1)))
print(preorderTraversal(TreeNode(1, TreeNode(2))))
print(preorderTraversal(TreeNode(1, None, TreeNode(2))))
