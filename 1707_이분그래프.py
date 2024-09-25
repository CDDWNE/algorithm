import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(s, g):
    visited[s] = g
    for n in graph[s]:
        if not visited[n]:
            a = dfs(n, -g)
            if not a:
                return False
        elif visited[n] == visited[s]:
            return False
    return True

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    for i in range(E):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    for j in range(1, V+1):
        if not visited[j]:
            result  = dfs(j, 1)
            if not result:
                break
    
    print("YES" if result else 'NO')