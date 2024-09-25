#%%

import sys
input = sys.stdin.readline

def dfs(s):
    ans_dfs.append(s)
    visited[s] = 1
    for i in graph[s]:
        if not visited[i]:
            dfs(i)

def bfs(s):
    q = []
    q.append(s)
    visited[s] = 1
    ans_bfs.append(s)
    
    while q:
        c = q.pop(0)
        for i in graph[c]:
            if not visited[i]:
                visited[i] = 1
                ans_bfs.append(i)
                q.append(i)

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(N+1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, N+1):
    graph[i].sort()

visited = [0] * (N+1)
ans_dfs = []
dfs(V)

visited = [0] * (N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)