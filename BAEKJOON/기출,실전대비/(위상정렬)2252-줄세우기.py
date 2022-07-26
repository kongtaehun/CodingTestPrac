#전형적인 위상정렬문제

from collections import deque


def topology_sort(q):
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)


# 위상정렬을 이용한다.
if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for i in range(n+1)]
    indegree = [0]*(n+1)
    for i in range(m):
        a, b = map(int, input().split())
        # a가 b보다 앞에서야하므로 진입차수를 b
        graph[a].append(b)
        indegree[b] += 1

    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    result = []
    topology_sort(q)
    for i in result:
        print(i,end= ' ')
