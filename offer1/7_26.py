class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

    def sub(A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return sub(A.left, B.left) and sub(A.right, B.right)

    return bool(A and B) and (sub(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))
