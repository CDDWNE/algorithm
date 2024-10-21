#%%

import sys
input = sys.stdin.readline

N = int(input())

table = [list(map(int, input().split())) for _ in range(N)]

table.sort(key= lambda x : (x[1], x[0]))
