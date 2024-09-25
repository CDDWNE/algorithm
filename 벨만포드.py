#%%

import sys
input = sys.stdin.readline

def bellman_ford(start):
    weights[start] = 0
    for i in range(V):
        for j in range(E):
            cur_node = graph[j][0]
            next_node = graph[j][1]
            weight = graph[j][2]

            if weights[cur_node] != INF and weights[next_node] > weight[cur_node] + weight:
                weights[next_node] = weights[cur_node] + weight
                
                if i == V - 1:
                    return True
    return False

INF = float('inf')
V, E = map(int, input().split())
graph = []

weights = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph.append((u, v, w))

negative_cycle = bellman_ford(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, V+1):
        if weights[i] == INF:
            print(-1)
        else:
            print(weights[i])