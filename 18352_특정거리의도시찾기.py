#%%

import sys
input = sys.stdin.readline
import heapq

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    INF = float('inf')
    weights = [INF] * (N+1)
    weights[start] = 0
    
    while heap:
        weight, node = heapq.heappop(heap)
        if weight > weights[node]:
            continue
        
        for n, w in graph[node]:
            W = weights[node] + w
            if weights[n] > W:
                weights[n] = W
                heapq.heappush(heap, (W, n))
    return weights

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append((y, 1))

ans = dijkstra(X)


count = 0

for i in range(N+1):
    if ans[i] == K:
        print(i)
        count += 1

if count == 0:
    print(-1)