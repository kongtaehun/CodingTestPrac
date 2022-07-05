from collections import deque

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
indegree = [0]*(n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


q = deque()
for i in range(1, len(indegree)):
    if indegree[i] == 0:
        q.append((i, 1))

result = [0 for i in range(n)]
while q:
    now, semester = q.popleft()
    result[now-1] = semester
    # 방문
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append((i, semester+1))

for i in result:
    print(i, end=' ')
