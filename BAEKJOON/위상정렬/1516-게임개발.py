import copy
from collections import deque

n = int(input())
indegree = [0 for i in range(n+1)]
duration = [0 for i in range(n+1)]
graph = [[] for i in range(n+1)]
for i in range(1, n+1):
    temp = list(map(int, input().split()))
    duration[i] = temp[0]
    for j in temp[1:-1]:
        graph[j].append(i)
        indegree[i] += 1

q = deque()
for i in range(0, len(indegree)):
    if indegree[i] == 0:
        q.append(i)


result = [0]*(n+1)

while q:
    now = q.popleft()
    result[now] += duration[now]
    for i in graph[now]:
        result[i] = max(result[i], result[now])
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)


for i in range(1, len(result)):
    print(result[i])
