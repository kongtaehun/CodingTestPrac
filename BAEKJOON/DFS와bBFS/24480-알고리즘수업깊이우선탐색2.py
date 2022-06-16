# =========confir==============
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# =========method=============

count = 1


def dfs(graph, visited, start):
    global count
    visited[start] = count
    count += 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(graph, visited, i)


# =========input==============
n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 정점별로 가장빠른 방문을 위해 각 배열 정렬
for i in graph:
    i.sort(reverse=True)
# =========main===============
dfs(graph, visited, start)
for i in range(1, n+1):
    print(visited[i])
