#%%

import sys
input = sys.stdin.readline

def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        c = q.pop(0)
        for i in tree[c]:
            if not visited[i]:
                visited[i] = c
                q.append(i)

N = int(input())

tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

visited = [0] * (N+1)

bfs(1)

for i in visited[2:]:
    print(i)