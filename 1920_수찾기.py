#%%

import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_list.sort() 

def lower_bound(arr, val):
    lo = 0
    hi = len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < val:
            lo = mid + 1
        else:
            hi = mid
    return lo

for x in M_list:
    idx = lower_bound(N_list, x)
    if idx < N and N_list[idx] == x:
        print(1)
    else:
        print(0)