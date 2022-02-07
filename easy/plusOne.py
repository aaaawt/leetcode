def plusOne(digits):
    k = 199
    i = len(digits) - 1
    while i >= 0 and k != 0:
        a = digits[i] + k
        digits[i] = a % 10
        k = a // 10
        i -= 1
    while k != 0:
        digits.insert(0, k % 10)
        k //= 10
    return digits

print(plusOne([1, 2, 3]))
print(plusOne([4, 3, 2, 1]))
print(plusOne([0]))
print(plusOne([9, 9, 9]))