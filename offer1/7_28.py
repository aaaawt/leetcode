class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric(root: TreeNode) -> bool:

    def subSymmetric(root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return (root1.val == root2.val) and subSymmetric(root1.left, root2.right) and subSymmetric(root1.right, root2.left)

    return subSymmetric(root, root)
