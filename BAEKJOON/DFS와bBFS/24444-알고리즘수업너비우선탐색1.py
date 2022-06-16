# ========config=========
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# ========method========

count = 1


def bfs(graph, visited, start):
    global count
    q = deque()
    visited[start] = count
    q.append(start)
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                count += 1
                visited[i] = count
                q.append(i)


# ========input=========
n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 정점별로 가장빠른 방문을 위해 각 배열 정렬
for i in graph:
    i.sort()

# =========main=========
bfs(graph, visited, start)
for i in range(1, n+1):
    print(visited[i])
