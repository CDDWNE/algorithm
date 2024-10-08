#%%

import sys
from collections import deque

input = sys.stdin.readline

v, e = map(int, input().split())

indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()
    
    for i in range(1, v+1):
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
        print(i)