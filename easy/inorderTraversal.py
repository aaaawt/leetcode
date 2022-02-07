from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def inorderTraversal(root:Optional[TreeNode]):
#     if not root:
#         return []
#     tree = []
#     tree.extend(inorderTraversal(root.left))
#     tree.append(root.val)
#     tree.extend(inorderTraversal(root.right))
#     return tree

def inorderTraversal(root:Optional[TreeNode]):
    def addLeft(node):
        while node:
            stack.append(node)
            node = node.left
    stack, tree = [], []
    addLeft(root)
    while stack:
        cur = stack.pop()
        tree.append(cur.val)
        addLeft(cur.right)
    return tree

print(inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))))
print(inorderTraversal(TreeNode()))
print(inorderTraversal(TreeNode(1, TreeNode(2, None, None), None)))
print(inorderTraversal(TreeNode(1, None, None)))
print(inorderTraversal(TreeNode(1, None, TreeNode(2, None, None))))