#%%
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))

lo = 0
hi = max(tree)

while lo < hi:
    mid = (lo + hi) // 2 + 1
    hap = sum([max(0, x - mid) for x in tree])
    if hap >= M:
        lo = mid
    else:
        hi = mid - 1
else:
    print(lo)