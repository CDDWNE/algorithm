#%%

import sys
input = sys.stdin.readline

N = int(input())

dp = [[0] for _ in range(N+1)]
for i in range(2, N+1):
    dp[i][0] = dp[i-1][0] + 1
    if i % 3 == 0:
        dp[i][0] = min(dp[i][0], dp[i // 3][0] + 1)
    if i % 2 == 0:
        dp[i][0] = min(dp[i][0], dp[i // 2][0] + 1)

print(dp)