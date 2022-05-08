# 动态规划 On O1
def numWays(n: int) -> int:
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a % 1000000007

print(numWays(2))
print(numWays(7))
print(numWays(0))
