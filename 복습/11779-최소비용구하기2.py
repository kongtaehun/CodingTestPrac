import heapq
INF = int(1e9)
# 최소비용과 경로!
# 역추적!
# 다익스트라 적용


def getRoute(start, end, route):
    result = []
    result.append(end)
    now = end
    while True:
        result.append(route[now])
        now = route[now]
        if now == start:
            break
    return result


def dijkstra(graph, distance, start, end):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                route[i[0]] = now
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    graph = [[] for i in range(n+1)]
    for i in range(m):
        start, end, cost = map(int, input().split())
        graph[start].append((end, cost))
    start, end = map(int, input().split())
    distance = [INF]*(n+1)
    # 경로상 전노드
    route = [0]*(n+1)
    dijkstra(graph, distance, start, end)
    print(distance[end])
    answer = getRoute(start, end, route)
    answer.reverse()
    print(len(answer))
    print(' '.join(list(map(str, answer))))
