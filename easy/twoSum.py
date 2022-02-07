nums = eval(input('nums:'))
target = eval(input('target:'))
ll = len(nums)
for i in range(ll):
    for j in range(i + 1, ll):
        if nums[i] + nums[j] == target:
            result = [i, j]
            print(result)
            break
    else:
        continue
    break

