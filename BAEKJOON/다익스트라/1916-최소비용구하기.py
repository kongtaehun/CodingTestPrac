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
            cost = dist+i[1]  # 지금까지의 비용 + 현재버스의비용
            if cost < distance[i[0]]:
                heapq.heappush(q, (cost, i[0]))
                distance[i[0]] = cost


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    graph = [[] for i in range(n+1)]
    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    start, end = map(int, input().split())
    distance = [INF]*(n+1)
    dijkstra(start)
    print(distance[end])
