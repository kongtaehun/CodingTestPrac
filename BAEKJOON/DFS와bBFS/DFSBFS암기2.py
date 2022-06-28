from collections import deque


def dfs(visited, graph, start):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(visited, graph, i)


def bfs(visited, graph, start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)


n = int(input())
m = int(input())
visited = [0]*(n+1)
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(visited, graph, 1)
print(visited)
