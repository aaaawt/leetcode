from typing import List

# 动态规划 On O1
def maxSubArray(nums: List[int]) -> int:
    maxsum = nums[0]
    start = 0
    for x in nums:
        start = max(start + x, x)  # !
        maxsum = max(maxsum, start)
    return maxsum

