import sys
from collections import deque
input = sys.stdin.readline


def bfs(start, visited):
    q = deque()
    q.append(start)
    visited[start] = 1
    print(start, end=' ')
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                print(i, end=' ')


def dfs(start, visited):
    visited[start] = 1
    print(start, end=' ')
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i, visited)


if __name__ == '__main__':
    n, m, v = map(int, input().split())
    graph = [[] for i in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        # 무방향상 그래프이므로 반대방향에 대한 정보도 입력
        graph[b].append(a)

    # 크기가 낮은 정점순서대로 방문하기 위한 정렬
    for i in graph:
        i.sort()

    visited = [0]*(n+1)
    dfs(v, visited)
    print()
    visited = [0]*(n+1)
    bfs(v, visited)
