import heapq
# 우선순위 위상정렬로
result = []


def topology_sort(q, indegree, graph):
    global result
    while q:
        now = heapq.heappop(q)
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, i)


def solution():
    global result
    n, m = map(int, input().split())
    graph = [[] for i in range(n+1)]
    indegree = [0]*(n+1)
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    q = []
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            heapq.heappush(q, i)
    topology_sort(q, indegree, graph)
    print(' '.join(list(map(str, result))))


solution()
