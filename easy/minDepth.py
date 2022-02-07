class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root: TreeNode):
    if not root:
        return 0
    if root.left and root.right:
        return min(minDepth(root.left), minDepth(root.right)) + 1
    return minDepth(root.left) + minDepth(root.right) + 1

    # if not root:
    #     return 0
    #
    # def depth(root):
    #     if not root:
    #         return 0xffffff
    #     if not root.left and not root.right:
    #         return 1
    #     return min(depth(root.left), depth(root.right)) + 1
    #
    # return depth(root)

print(minDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
print(minDepth(TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))))
print(minDepth(None))