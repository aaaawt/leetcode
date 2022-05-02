# 时间复杂度On，空间复杂度On，不改变原数组
def findRepeatNumber1(self, nums: List[int]) -> int:
    visited = set()
    for x in nums:
        if x not in visited:
            visited.add(x)
        else:
            return x

def findRepeatNumber2(self, nums: List[int]) -> int:
    visited = [False]*len(nums)
    for x in nums:
        if not visited[x]:
            visited[x] = True
        else:
            return x

# 时间复杂度Onlogn，空间复杂度O1，不改变原数组
def findRepeatNumber3(self, nums: List[int]) -> int:
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]

# 时间复杂度On，空间复杂度O1，改变原数组
def findRepeatNumber4(self, nums: List[int]) -> int:
    for i, x in enumerate(nums):
        while i != x:
            if nums[x] != x:
                nums[i], nums[x] = nums[x], x
            else:
                return x
