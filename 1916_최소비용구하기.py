#%%

import sys
input = sys.stdin.readline
import heapq

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

        for w, n in graph[node]:
            W = weights[node] + w
            if weights[n] > W:
                weights[n] = W
                heapq.heappush(heap, (W, n))
                
    return weights

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

start, dst = map(int, input().split())
ans = dijkstra(start)
print(ans[dst])