from typing import List

# 时间复杂度On，空间复杂度O1
def minArray1(numbers: List[int]) -> int:
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            return numbers[i]
    return numbers[0]

# 时间复杂度Ologn，空间复杂度O1
def minArray2(numbers: List[int]) -> int:
    left = 0
    right = len(numbers) - 1
    while left != right:
        m = (left + right) // 2
        if numbers[m] < numbers[right]:
            right = m
        elif numbers[m] > numbers[right]:
            left = m + 1
        else:
            right -= 1
    return numbers[left]
