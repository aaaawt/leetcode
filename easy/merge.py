def merge(nums1, m, nums2, n):
    if m == 0:
        for i in range(len(nums1)):
            nums1[i] = nums2[i]
    n = len(nums1) - 1
    i = m - 1
    j = len(nums2) - 1
    while i >= 0 and j >= 0:
        if nums1[i] < nums2[j]:
            nums1[n] = nums2[j]
            nums1[n-1] = nums1[i]
            j -= 1
        else:
            nums1[n] = nums1[i]
            nums1[n - 1] = nums2[j]
            i -= 1
        n -= 1
    if i < 0 and j >= 0:
        for k in range(j):
            nums1[k] = nums2[k]
    return nums1

print(merge([2, 0], 1, [1], 1))
print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(merge([1], 1, [], 0))
print(merge([0], 0, [1], 1))
print(merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3))
