def lettercombinations(digits):
    if digits == '':
        return []
    # 回溯
    nums = [f'{i}' for i in range(2, 10)]
    words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    dd = dict(zip(nums, words))

    def drawback(index):
        if index == len(digits):
            ans.append(''.join(ll))
            return
        for x in dd[digits[index]]:
            ll.append(x)
            drawback(index + 1)
            ll.pop()

    ll = []
    ans = []
    drawback(0)
    return ans
    # 循环
    # nums = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    # ll = ['']
    # for x in digits:
    #     res = []
    #     for j in ll:
    #         for i in nums[int(x) - 2]:
    #             res.append(j + i)
    #     ll = res
    # return ll

print(letterCombinations('3456'))
print(letterCombinations('23'))
print(letterCombinations(''))
print(letterCombinations('2'))
