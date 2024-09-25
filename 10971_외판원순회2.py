#%%

import sys
input = sys.stdin.readline

n = int(input())
num_list = [list(map(int, input().split())) for _ in range(n)]
print(num_list)

for li in num_list:
    now = 0
    z_count = 0
    for i in range(n):
        