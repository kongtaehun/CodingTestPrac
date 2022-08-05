import copy
from collections import deque
# 위상정렬


def topology_sort(indegree, graph):
    global result, origin_costs
    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            # 방문하면 무조건 비용초기화
            # 방문하고 원래비용과 DP비용을 나눠서 계산해야함
            costs[i] = max(costs[i], costs[now]+origin_costs[i])
            if indegree[i] == 0:
                q.append(i)


if __name__ == '__main__':
    n = int(input())
    parant = [i for i in range(n)]
    graph = [[] for i in range(n)]
    costs = [0]*(n)
    indegree = [0]*(n)
    for i in range(n):
        tmp = list(map(int, input().split()))
        costs[i] = tmp[0]
        for j in range(tmp[1]):
            graph[tmp[2+j]-1].append(i)
            indegree[i] += 1
    origin_costs = copy.deepcopy(costs)
    result = []
    topology_sort(indegree, graph)
    # print(result)
    print(max(costs))
    # for i in result:
    #     print(i+1, end=' ')

    # print(costs)
    # 같은 위계에서 가장 높은 cost를 가진 것을 선택
