# 무방향성
# 비연결성
from collections import deque


def bfs(start, visited):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    graph = [[] for i in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0]*(n+1)

    bfs(1, visited)
    print(sum(visited)-1)
