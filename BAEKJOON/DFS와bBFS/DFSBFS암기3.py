from collections import deque


def dfs(graph, visited, start):
    global count
    count += 1
    visited[start] = count
    for i in graph[start]:
        if visited[i] == 0:
            dfs(graph, visited, i)


def bfs(graph, visited, start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1


n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0 for i in range(n+1)]
count = 0
dfs(graph, visited, v)
print(visited)
