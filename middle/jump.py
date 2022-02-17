def jump(nums):
    n = len(nums)
    far = 0
    count = 0
    end = 0
    for i in range(n - 1):
        if i <= far:
            far = max(far, i + nums[i])
            if i == end:
                end = far
                count += 1
    return count


    # if len(nums) == 1:
    #     return 0
    # n = len(nums) - 1
    # count = 0
    # while n != 1:
    #     if nums[0] >= n:
    #         break
    #     for i in range(1, n):
    #         if nums[i] >= n - i:
    #             n = i
    #             break
    #     count += 1
    # return count + 1


print(jump([1]))
print(jump([3, 2, 5, 6, 1, 3, 8, 1, 5, 3, 2, 4, 1]))
print(jump([2, 3, 1, 1, 4]))
print(jump([2, 3, 0, 1, 4]))
