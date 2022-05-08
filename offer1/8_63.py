from typing import List

# 动态规划 On O1
def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0
    a = prices[0]
    profix = 0
    for x in prices:
        a = min(a, x)
        profix = max(x - a, profix)
    return profix

print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
print(maxProfit([]))
