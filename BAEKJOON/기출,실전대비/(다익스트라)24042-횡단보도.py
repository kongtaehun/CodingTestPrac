import sys
import heapq


def dijkstra(distance, graph, mx):

    q = []
    heapq.heappush(q, (0, 0, 1))  # cost,order
    distance[1] = 0
    while q:
        # print(distance)
        dist, order, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for next_ord, next in graph[now]:

            if next_ord > order:
                cost = dist+(next_ord-order)
                if cost < distance[next]:
                    heapq.heappush(q, (cost, next_ord, next))
                    distance[next] = cost
            else:
                cost = findClosestGCD(dist, mx) + next_ord
                if cost < distance[next]:
                    heapq.heappush(q, (cost, next_ord, next))
                    distance[next] = cost


def findClosestGCD(now, mx):
    if now % mx == 0:
        return mx*(now//mx)
    else:
        return mx*(now//mx+1)


def solution():
    # 중복이 있을 수도 있다는 사실!
    n, mx = map(int, input().split())
    graph = [[] for i in range(n+1)]
    for i in range(mx):
        a, b = map(int, input().split())
        graph[a].append((i+1, b))
        graph[b].append((i+1, a))
    distance = [sys.maxsize]*(n+1)
    dijkstra(distance, graph, mx)
    print(distance[n])
    # print(graph)


solution()
