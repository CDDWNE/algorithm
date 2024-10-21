#%%

import sys
input = sys.stdin.readline
from collections import deque

def bfs(a, b):
    q = deque()
    graph[a][b] = 0
    q.append((a, b))
    count = 1
    while q:
        x, y  = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                count += 1
    return count
N = int(input())
graph = []


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    graph.append(list(map(int, input().strip())))

cnt = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt.append(bfs(i, j))
cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])