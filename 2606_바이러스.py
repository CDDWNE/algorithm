#%%

import sys
input = sys.stdin.readline

def dfs(s):
    global count
    visited[s] = 1
    for i in graph[s]:
        if not visited[i]:
            count += 1
            dfs(i)

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1,N+1):
    graph[i].sort()

count = 0
dfs(1)
print(count)