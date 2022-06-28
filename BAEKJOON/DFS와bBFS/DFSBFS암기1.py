from collections import deque


def dfs(graph, visited, start):
    global dfs_result
    visited[start] = 1
    dfs_result.append(start)
    for i in graph[start]:
        if visited[i] == 0:
            dfs(graph, visited, i)


def bfs(graph, visited, start):
    global bfs_result
    q = deque()
    q.append(start)
    bfs_result.append(start)
    visited[start] = 1
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                bfs_result.append(i)
                visited[i] = 1
                q.append(i)


n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()


visited = [0 for i in range(n+1)]
dfs_result = []
bfs_result = []

graph_for_bfs = graph[:]
start_for_bfs = start
dfs(graph, visited, start)
visited = [0 for i in range(n+1)]
bfs(graph_for_bfs, visited, start_for_bfs)
print(dfs_result)
print(bfs_result)
