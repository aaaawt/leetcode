class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return '(%d %s %s)' % (self.val, self.left, self.right)

def sortedArrayToBST(nums):
    def arrayToBST(left, right):
        if left == right:
            return None
        m = (left + right) // 2
        root = TreeNode(nums[m])
        root.left = arrayToBST(left, m)
        root.right = arrayToBST(m + 1, right)
        return root
    return arrayToBST(0, len(nums))


print(sortedArrayToBST([-10, -3, 0, 5, 9]))
print(sortedArrayToBST([1, 3]))
