def singleNumber(nums):
    res = 0
    for i in nums:
        res = i ^ res
    return res

    # ss = set()
    # for i in nums:
    #     if i not in ss:
    #         ss.add(i)
    #     else:
    #         ss.remove(i)
    # return list(ss)[0]

print(singleNumber([2, 2, 1]))
print(singleNumber([4, 1, 2, 1, 2]))