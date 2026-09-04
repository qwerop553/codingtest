triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

dp = [[0] * (len(triangle)+2) for _ in range(len(triangle))]

dp[0][1] = triangle[0][0]
for level in triangle[1:]:
    n = len(level)
    for i, node in enumerate(level, start=1):
        dp[n-1][i] = max(dp[n-2][i-1], dp[n-2][i], dp[n-2][i+1]) + node if i != 1 else max(dp[n-2][i-1], dp[n-2][i]) + node 

print(max(dp[len(triangle)-1]))

def solution(triangle):
    dp = [[0] * (len(triangle)+2) for _ in range(len(triangle))]

    dp[0][1] = triangle[0][0]
    for level in triangle[1:]:
        n = len(level)
        for i, node in enumerate(level, start=1):
            dp[n-1][i] = max(dp[n-2][i-1], dp[n-2][i]) + node 

    return max(dp[len(triangle)-1])