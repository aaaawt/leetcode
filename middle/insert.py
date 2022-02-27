def insert(intervals, newInterval):
    left, right = newInterval
    res = []
    placed = False
    for i, j in intervals:
        if i > right:
            if not placed:
                res.append([left, right])
                placed = True
            res.append([i, j])
        elif j < left:
            res.append([i, j])
        else:
            left = min(left, i)
            right = max(right, j)

    if not placed:
        res.append([left, right])
    return res


print(insert([[1, 3], [6, 9]], [2, 5]))
print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
print(insert([[1, 5]], [2, 3]))
print(insert([], [5, 7]))
print(insert([[1, 5]], [2, 7]))
