#%%

import sys
input = sys.stdin.readline

N = int(input())

plate = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (N) for _ in range(N)]

dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            break
        if i + plate[i][j] < N:
            dp[i + plate[i][j]][j] += dp[i][j]
        if j + plate[i][j] < N:
            dp[i][j + plate[i][j]] += dp[i][j] 

print(dp[-1][-1])