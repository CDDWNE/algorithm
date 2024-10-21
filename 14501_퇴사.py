#%%

import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)
coun = [list(map(int, input().split())) for _ in range(N)]


for i in range(N-1, -1, -1):
    if i + coun[i][1] > N:
        dp[i] = dp[i+1]


print(dp[-1])