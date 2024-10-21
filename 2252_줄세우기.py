#%%

import sys
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())

def topo():
    result = []
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft()
        result.append(now)
        
        for g in graph[now]:
            indegree[g] -= 1
            if indegree[g] == 0:
                q.append(g)
    for i in result:
        print(i, end=' ')


graph = [[] for _ in range(N + 1)]
indegree = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
topo()