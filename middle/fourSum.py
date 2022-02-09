class Num:
    def __init__(self, val: int, count: int = 1) -> None:
        self.val = val
        self.count = count

def fourSum(nums, target):
    results = []
    nums.sort()
    grouped_nums = []
    for i in nums:
        if grouped_nums and grouped_nums[-1].val == i:
            grouped_nums[-1].count += 1
        else:
            grouped_nums.append(Num(i))
    hash_table = {i.val: i for i in grouped_nums}
    for a_idx, a in enumerate(grouped_nums):
        if 4 * a.val > target:
            break
        a.count -= 1
        for b_idx in range(a_idx if a.count else a_idx + 1, len(grouped_nums)):
            b = grouped_nums[b_idx]
            if a.val + b.val * 3 > target:
                break
            b.count -= 1
            for c_idx in range(b_idx if b.count else b_idx + 1, len(grouped_nums)):
                c = grouped_nums[c_idx]
                if a.val + b.val + 2 * c.val > target:
                    break
                c.count -= 1
                d = target - a.val - b.val - c.val
                if d in hash_table and hash_table[d].count >= 1:
                    results.append([a.val, b.val, c.val, d])
                c.count += 1
            b.count += 1
        a.count += 1
    return results


print(fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11))
print(fourSum([1, 0, -1, 0, -2, 2], 0))
print(fourSum([2, 2, 2, 2, 2], 8))
