import heapq
INF = int(1e9)


def dijkstra(distance, graph, start, end):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for edge in graph[now]:
            cost = dist+edge[1]
            if cost < distance[edge[0]]:
                distance[edge[0]] = cost
                route[edge[0]] = now
                heapq.heappush(q, (cost, edge[0]))


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    distance = [INF]*(n+1)
    graph = [[] for i in range(n+1)]
    route = [0 for i in range(n+1)]
    for i in range(m):
        a, b, cost = map(int, input().split())
        graph[a].append((b, cost))
    start, end = map(int, input().split())
    dijkstra(distance, graph, start, end)

    # 역추적
    i = end
    result = []
    result.append(end)
    while True:
        result.append(route[i])
        i = route[i]
        if i == start:
            break
    result.reverse()

    print(distance[end])
    print(len(result))
    for i in result:
        print(i, end=' ')
