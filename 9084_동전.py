#%%

import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())
    dp = [0]*(M+max(coin))

    for k in coin:
        dp[k] += 1
        for j in range(k+1, M+k):
            dp[j] = dp[j - k] + dp[j]
    
    print(dp[M])


            



