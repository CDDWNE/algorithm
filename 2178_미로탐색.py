import sys
input = sys.stdin.readline
from collections import deque
def bfs(a, b):
    q = deque()
    q.append((a, b))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return graph[N-1][M-1]

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip())))
    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
print(bfs(0, 0))