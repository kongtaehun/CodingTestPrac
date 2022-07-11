from collections import deque


def bfs(start, visited):
    global result
    q = deque()
    q.append((start, 0))
    while q:
        now, cost = q.popleft()
        if now == n:
            break
        for i in graph[now]:
            if visited[i[0]] == 0 or visited[i[0]] > cost+i[1]:
                q.append((i[0], cost+i[1]))
                visited[i[0]] = cost+i[1]


# 다익스트라를 사용해야할 떄가 된건가?
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [0]*(n+1)
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for i in graph:
    i.sort(key=lambda x: x[1])
result = 0
bfs(1, visited)
print(visited[n])
