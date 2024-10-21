#%%
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

stuff = []
for i in range(N):
    w, v = map(int, input().split())
    stuff.append((w, v))
dp = [0] * (K+1)

for item in stuff:
    W, P = item
    for i in range(K, W-1, -1):
        dp[i] = max(dp[i], dp[i-W] + P)
print(dp[K])

