class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: TreeNode):
    if not root:
        return True
    def isEqual(p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return isEqual(p.left, q.right) and isEqual(p.right, q.left)
        else:
            return False
    return isEqual(root.left, root.right)


print(isSymmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))))
print(isSymmetric(TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))))
