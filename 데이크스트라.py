#%%

import heapq

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    INF = float('inf')
    weights = [INF] * (vertex + 1)
    weights[start] = 0

    while heap:
        weight, node = heapq.heappop(heap)
        if weight > weights[node]:
            continue

        for n, w in graph[node]:
            W = weight + w
            if weights[n] > W:
                weights[n] = W
                heapq.heappush(heap, (W, n))
    return weights

vertex, edge, start = map(int, input().split())
graph = [[] for _ in range(vertex + 1)]
for _ in range(edge):
    src, dst, weight = map(int, input().split())
    graph[src].append((dst, weight))
    
weights = dijkstra(start)

for i in range(1, vertex + 1):
    if weights[i] == float('inf'):
        print('INF')
    else:
        print(weights[i])