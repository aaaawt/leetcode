def search2(nums, target):
    for num in nums:
        if num == target:
            return True
    return False


print(search2([2, 5, 6, 0, 0, 1, 2], 0))
print(search2([2, 5, 6, 0, 0, 1, 2], 3))
