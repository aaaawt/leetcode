def maxProfit(prices):
    ma = 0
    mi = prices[0]
    for i in range(len(prices)):
        ma = max(ma, prices[i] - mi)
        mi = min(mi, prices[i])
    return ma

print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
print(maxProfit([7]))