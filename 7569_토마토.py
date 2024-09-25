#%%

import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
graph = []
for i in range(N * H):
    graph.append(list(map(int, input().split())))

print(graph)