def letterCombinations(digits):
    if digits == '':
        return []
    nums = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    ll = ['']
    for x in digits:
        res = []
        for j in ll:
            for i in nums[int(x) - 2]:
                res.append(j + i)
        ll = res
    return ll

print(letterCombinations('3456'))
print(letterCombinations('23'))
print(letterCombinations(''))
print(letterCombinations('2'))