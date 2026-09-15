n = 5
money = [1, 2, 5]

dp = [[-1] * len(money) for _ in range(n+1)]

def solve(n, money):
    m = len(money) - 1
    if m == 0: return 1 if n % money[0] == 0 else 0
    
    *rest, last = money
    if dp[n][m] != -1:
        return dp[n][m]
    dp[n][m] = sum(solve(n-i, rest) for i in range(0, n+1, last))
    return dp[n][m]

print(dp)
print(solve(n, money))
print(dp)
