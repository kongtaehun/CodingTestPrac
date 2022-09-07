# 다익스트라 알고리즘
# 크루스칼알고리즘
import heapq
INF = int(1e9)


def dijkstra(graph, distance, start):
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for cost, node in graph[now]:
            temp = cost+dist
            if temp < distance[node]:
                distance[node] = temp
                heapq.heappush(q, (node, temp))


if __name__ == '__main__':
    for _ in range(int(input())):
        n, d, s = map(int, input().split())
        graph = [[] for i in range(n+1)]
        for i in range(d):
            a, b, c = map(int, input().split())
            graph[b].append((c, a))
        distance = [INF]*(n+1)
        dijkstra(graph, distance, s)
        # print(distance)

        val = 0
        cnt = 0
        for i in distance:
            if i != INF:
                cnt += 1
                val = max(i, val)
        print(cnt, val)
