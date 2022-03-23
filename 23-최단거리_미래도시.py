# 다익스트라 알고리즘으로 풀었다
import heapq
'''

n, m = map(int, input().split())
INF = int(1e9)
distance = [INF for i in range(n+1)]
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
x, k = map(int, input().split())


def dijstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijstra(1)
dist_x = distance[k]
distance = [INF for i in range(n+1)]
dijstra(x)
result = dist_x+distance[k]
print(result)
'''

# 플루드 워셜 알고리즘
n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0


for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    # 왕복까지 포함
    graph[b][a] = 1
x, k = map(int, input().split())

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

result = graph[1][k]+graph[k][x]
print(result)

for i in range(n+1):
    for j in range(n+1):
        print(graph[i][j], end=' ')
