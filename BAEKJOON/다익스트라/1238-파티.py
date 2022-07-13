import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            node = i[0]
            if cost < distance[node]:
                heapq.heappush(q, (cost, node))
                distance[node] = cost


if __name__ == '__main__':
    n, m, x = map(int, input().split())
    graph = [[] for i in range(n+1)]
    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    # 출발점 -> 각 마을에서부터 x마을까지

    total_cost = [0]*(n+1)
    for i in range(1, n+1):
        distance = [INF]*(n+1)
        dijkstra(i)
        total_cost[i] = distance[x]

    # 도착점 -> x에서부터 각마을까지
    distance = [INF]*(n+1)
    dijkstra(x)
    for i in range(1, len(distance)):
        total_cost[i] += distance[i]
    print(max(total_cost))
