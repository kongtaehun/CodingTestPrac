from collections import deque


def bfs(graph, visited, start):
    q = deque()
    visited[start] = 1
    q.append(start)
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for i in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[b].append(a)

    result = []
    result_val = 0
    for i in range(1, n+1):
        visited = [0]*(n+1)
        bfs(graph, visited, i)
        temp = sum(visited)
        if result_val == temp:
            result.append(i)
        elif result_val < temp:
            result = [i]
            result_val = temp
    result.sort()
    print(' '.join(list(map(str, result))))
