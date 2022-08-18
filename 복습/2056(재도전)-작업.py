from collections import deque
import copy


def topology_sort(q):
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            costs[i] = max(costs[i], costs[now]+origin_cost[i])
            if indegree[i] == 0:
                q.append(i)


# 위상정렬!
if __name__ == '__main__':
    n = int(input())
    graph = [[] for i in range(n+1)]

    origin_cost = [0]*(n+1)
    indegree = [0]*(n+1)
    for i in range(n):
        temp = list(map(int, input().split()))
        origin_cost[i+1] = temp[0]
        if temp[1] != 0:
            for b in temp[2:]:
                graph[b].append(i+1)  # 순서에 유의
                indegree[i+1] += 1
    costs = copy.deepcopy(origin_cost)
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    steps = [0]*(n+1)
    result = []
    topology_sort(q)
    # print(result)
    print(max(costs))
