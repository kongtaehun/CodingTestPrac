from collections import deque

# bfs로 가보자잉


def bfs(graph, visited, start, cnt):
    q = deque()
    q.append(start)
    visited[start] = cnt
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = cnt


if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for i in range(n+1)]
    visited = [0]*(n+1)
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    cnt = 1
    for i in range(1, n+1):
        if visited[i] == 0:
            bfs(graph, visited, i, cnt)
            cnt += 1

    print(max(visited))
