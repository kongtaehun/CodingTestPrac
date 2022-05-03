import bisect
import heapq
# 입력
n, m = map(int, input().split())
INF = int(1e9)
distance = [INF]*(n+1)
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (distance[i], i))


a = [1, 2, 3, 3, 5, 10]
x = 3


bisect.bisect_left(a, x)  # 2
bisect.bisect_right(a, x)  # 4

dijkstra(1)

max_result = 0
for i in range(1, len(distance)):
    if distance[i] < 1e9:
        max_result = max(distance[i], max_result)
idx = []
for i in range(1, len(distance)):
    if distance[i] == max_result:
        idx.append(i)

idx_min = min(idx)
cnt = len(idx)
print(idx_min, max_result, cnt)
