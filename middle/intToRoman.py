def intToRoman(num):
    value = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    value.reverse()
    roman.reverse()
    res = ''
    i = 0
    while i < len(value):
        if num >= value[i]:
            res += roman[i]
            num = num - value[i]
        else:
            i += 1
    return res

print(intToRoman(3))
print(intToRoman(4))
print(intToRoman(9))
print(intToRoman(58))
print(intToRoman(1994))
