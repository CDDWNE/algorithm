#%%

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(n):
    visited[n] = 1
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N+1):
    graph[i].sort()

visited = [0] * (N+1)
count = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1
    else:
        pass
    
print(count)