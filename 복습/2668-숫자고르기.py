from collections import deque
# 사이클판별
# 방향성있음!
# 비연결성 그래프임!
# 노드하나하나 검사하면서 다시 자신에게 돌아오면


def bfs(start, graph):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        now = q.popleft()
        for i in graph[now]:
            if i == start:
                return True
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
    return False


if __name__ == '__main__':
    n = int(input())
    result = []
    graph = [[] for i in range(n+1)]
    for i in range(1, n+1):
        graph[i].append(int(input()))
    for i in range(1, n+1):
        visited = [0]*(n+1)
        if bfs(i, graph):
            result.append(i)
    result.sort()
    print(len(result))
    for i in result:
        print(i)
