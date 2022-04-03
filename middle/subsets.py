def subsets(nums):
    ans = [[]]
    for i in range(len(nums)-1, -1, -1):
        for ll in ans[:]:
            ans.append(ll + [nums[i]])
    return ans

print(subsets([1, 2, 3]))
print(subsets([0]))
