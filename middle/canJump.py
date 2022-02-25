def canJump(nums):
    n = len(nums)
    far = 0
    for i in range(n):
        if i <= far:
            far = max(far, i + nums[i])
        if far >= n - 1:
            return True
    return False

print(canJump([2, 3, 1, 1, 4]))
print(canJump([3, 2, 1, 0, 4]))
print(canJump([2, 0, 0]))
print(canJump([0]))
