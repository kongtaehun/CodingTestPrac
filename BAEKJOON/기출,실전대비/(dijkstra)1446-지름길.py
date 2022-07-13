import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
MAX_IDX = 10001


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = i[1]+dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 모든점을 비용이 1인 노드로 간주
if __name__ == '__main__':
    n, d = map(int, input().split())
    graph = [[] for i in range(MAX_IDX)]
    for i in range(n):
        a, b, c = list(map(int, input().split()))
        # 아낄수 있는 비용
        graph[a].append((b, c))
    for i in range(d+1):
        graph[i].append((i+1, 1))

    distance = [INF]*(MAX_IDX)

    dijkstra(0)
    print(distance[d])
