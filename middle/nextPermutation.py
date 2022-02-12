def nextPermutation(nums):
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] > nums[i - 1]:
            break
    else:
        nums.reverse()
        return
    for j in range(len(nums) - 1, i - 1, -1):
        if nums[j] > nums[i - 1]:
            break
    nums[j], nums[i - 1] = nums[i - 1], nums[j]
    nums[i:] = nums[len(nums) - 1:i - 1:-1]

a = [1, 1, 5]
copy = a[:]
while True:
    print(a)
    nextPermutation(a)
    if copy == a:
        break
# a = [2, 3, 2]
# nextPermutation(a)
# print(a)
# b = [1, 2, 3]
# nextPermutation(b)
# print(b)


