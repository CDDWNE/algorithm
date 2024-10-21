#%%

import sys
input = sys.stdin.readline
from collections import deque
def bfs(a, b):
    cur = graph[a][b]
    graph[a][b] = 'o'
    q = deque()
    q.append((a, b))
    count = 1
    while q:
        x, y = q.popleft()
        
        nx = x + 1
        ny = y + 1
        
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if graph[nx][ny] == cur:
            graph[nx][ny] = 'o'
            q.append((nx, ny))

    return count

N, M = map(int, input().split())
graph = []
for i in range(M):
    graph.append(list(input().strip()))

total = []
for i in range(N):
    for j in range(M):
        if graph[i][j] != 'o':
            total.append(bfs(i, j))

print(total)
        