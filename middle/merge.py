def merge(intervals):
    intervals.sort()
    n = len(intervals)
    res = []
    left = intervals[0][0]
    right = intervals[0][1]
    for i in range(1, n):
        if right < intervals[i][0]:
            res.append([left, right])
            left, right = intervals[i][0], intervals[i][1]
        else:
            right = max(right, intervals[i][1])
    res.append([left, right])
    return res

print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge([[1, 4], [4, 5]]))
