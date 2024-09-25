#%%

import sys
input = sys.stdin.readline

class Graph:
    
    def __init__(self, vertex) -> None:
        self.V = vertex
        self.graph = []
    
    def add_Edge(self, u, v, w):
        self.graph.append([u, v, w])
    
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]
    
    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x 
            rank[x] += 1
    
    def Kruskal(self):
        result = []
        i = 0
        e = 0
        
        self.graph = sorted(self.graph, key=lambda item: item[2])
        
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        
        minimumCost = 0
        for u, v, w in result:
            minimumCost += w
        print(minimumCost)
            
V, E = map(int, input().split())

g = Graph(V)
for _ in range(E):
    u, v, w = map(int, input().split())
    g.add_Edge(u-1, v-1, w)
g.Kruskal()
# %%