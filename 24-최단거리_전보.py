import heapq
n, m, cc = map(int, input().split())
INF = int(1e9)
graph = [[] for i in range(n+1)]
distance = [INF for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            if distance[i[0]] > i[1]+dist:
                heapq.heappush(q, (i[1]+dist, i[0]))
                distance[i[0]] = i[1]+dist


dijstra(cc)

count = 0
max = 0
for i in range(len(distance)):
    if distance[i] >= 1 and distance[i] < int(1e9):
        count += 1
        if max < distance[i]:
            max = distance[i]

print(str(count)+" "+str(max))
