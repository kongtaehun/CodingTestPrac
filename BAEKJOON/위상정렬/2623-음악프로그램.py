from collections import deque

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
indegree = [0]*(n+1)
for i in range(m):
    temp = list(map(int, input().split()))
    for i in range(1, len(temp)-1):
        graph[temp[i]].append(temp[i+1])
        indegree[temp[i+1]] += 1


q = deque()
for i in range(1, len(indegree)):
    if indegree[i] == 0:
        q.append(i)

result = []
while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

if len(result) < n:
    print(0)
else:
    for i in result:
        print(i)
