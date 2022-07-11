# dijkstra
# distance
# heapq
import sys
import heapq
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
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


if __name__ == '__main__':
    v, e = map(int, input().split())
    s = int(input())
    graph = [[] for i in range(v+1)]
    for i in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    distance = [INF]*(v+1)
    dijkstra(s)
    for i in range(1, len(distance)):
        print('INF'if distance[i] == INF else distance[i])
