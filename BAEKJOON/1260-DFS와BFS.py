from collections import deque
n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for i in range(n+1)]


def dfs(start):
    print(start, end=' ')
    visited[start] = 1
    for i in sorted(graph[start]):
        if visited[i] == 0:
            dfs(i)


dfs(start)
print()

visited = [0 for i in range(n+1)]
q = deque()
q.append(start)
visited[start] = 1
while q:
    now = q.popleft()
    print(now, end=' ')
    for i in sorted(graph[now]):
        if visited[i] == 0:
            visited[i] = 1
            q.append(i)
