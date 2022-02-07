def maxArea(height):
    left = 0
    right = -1
    maxarea = 0
    while left != len(height) + right:
        k = len(height) + right - left
        if height[left] < height[right]:
            area = k * height[left]
            left += 1
        else:
            area = k * height[right]
            right -= 1
        maxarea = max(maxarea, area)
    return maxarea

print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea([1, 1]))
print(maxArea([4, 3, 2, 1, 4]))
print(maxArea([1, 2, 1]))