#%%

import sys
input = sys.stdin.readline

row, col = map(int, input().split())

graph = []

for i in range(row):
    graph.append(list(map(int, input().split())))
print(graph)