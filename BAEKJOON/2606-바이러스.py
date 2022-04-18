n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
start = 1
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0


def dfs(start):
    global count
    visited[start] = 1
    count += 1
    for i in graph[start]:
        if visited[i] == 0:

            dfs(i)


dfs(start)
print(count - 1)
