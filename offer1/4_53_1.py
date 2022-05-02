# 时间复杂度Ologn+（target出现的个数），空间复杂度O1
def search(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)
    while left != right:
        m = (left + right) // 2
        if nums[m] == target:
            break
        elif nums[m] < target:
            left = m + 1
        else:
            right = m
    if left == right:
        return 0
    count = 1
    left = m - 1
    while left >= 0 and nums[left] == target:
        count += 1
        left -= 1
    right = m + 1
    while right < len(nums) and nums[right] == target:
        count += 1
        right += 1
    return count
