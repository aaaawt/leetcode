class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def mirrorTree1(root: TreeNode) -> TreeNode:
    if not root:
        return None
    ans = TreeNode(0)

    def dfs(root, ans):
        if root:
            ans.val = root.val
        else:
            return
        if root.left:
            ans.right = TreeNode(0)
            dfs(root.left, ans.right)
        if root.right:
            ans.left = TreeNode(0)
            dfs(root.right, ans.left)

    dfs(root, ans)
    return ans

def mirrorTree2(root: TreeNode) -> TreeNode:
    if not root:
        return root
    left = mirrorTree2(root.left)
    right = mirrorTree2(root.right)
    root.left, root.right = right, left
    return root
