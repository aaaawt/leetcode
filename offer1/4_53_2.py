# 时间复杂度On，空间复杂度O1
from typing import List


def missingNumber1(nums: List[int]) -> int:
    for i, x in enumerate(nums):
        if i != x:
            return i
    return len(nums)

# 时间复杂度Ologn，空间复杂度O1
def missingNumber2(nums: List[int]) -> int:
    left = 0
    right = len(nums)
    while left != right:
        m = (left + right) // 2
        if m == nums[m]:
            left = m + 1
        else:
            right = m
    return left

print(missingNumber2([0]))
