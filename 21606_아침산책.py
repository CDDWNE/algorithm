import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
a = input().rstrip()

graph = [[] for _ in range(n+1)]
place = [0] * (n+1)
visited = [0] * (n+1)

for i in range(len(a)):
    if a[i] == '1':
        place[i+1] = 1

for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(node):
    res = 0
    for next_node in graph[node]:
        if place[next_node] == 0:
            if not visited[next_node]:
                visited[next_node] = 1
                res += dfs(next_node)
        else:
            res += 1
    return res

ans = 0
for i in range(1, n+1):
    if place[i] == 0:
        if not visited[i]:
            visited[i] = 1
            res = dfs(i)
            ans += res * (res - 1)
    else:
        for next_node in graph[i]:
            if place[next_node] == 1:
                ans += 1
                
                
print(ans)