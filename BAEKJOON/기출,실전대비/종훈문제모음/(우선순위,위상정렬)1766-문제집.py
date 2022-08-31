#다음에 꺼낼 수 있는 것들 중에 가장 갚이 낮은 값을 꺼낸다
# 정렬하면서 값을 꺼낼 수 있다.!

from collections import deque
import heapq
# 위상정렬?


def topology_sort(q):
    global result
    while q:
        now = heapq.heappop(q)
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, i)


if __name__ == '__main__':
    n, m = map(int, input().split())

    graph = [[] for i in range(n+1)]
    indegree = [0]*(n+1)
    result = []
    # 4보다2가 먼저 3보다 1이 먼저인 경우에서 가장 내림차순
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    q = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(q, i)

    topology_sort(q)
    print(' '.join(list(map(str, result))))
