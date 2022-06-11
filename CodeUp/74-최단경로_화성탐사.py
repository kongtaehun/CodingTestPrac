import heapq
INF = int(1e9)
t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
result = []
# 출발점으로부터 각점의 최단거리저장


def dijkstra(x, y):
    q = []
    # 우선순위 힙에다가 (비용, 노드)순서로 입력
    heapq.heappush(q, (0, x, y))
    # 거리 초기화
    distance[x][y] = 0
    # q가 끝날 때까지
    while q:
        dist, x, y = heapq.heappop(q)
        # 현재 거리가 dp저장된거리보다 작을 때 건너뛰기
        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue
            # 현재까지의 비용과 연결된 노드비용
            cost = dist+graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))


for _ in range(t):
    n = int(input())
    distance = [[INF]*(n) for i in range(n)]
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    dijkstra(0, 0)

    result.append(distance[n-1][n-1]+graph[0][0])
    for i in range(n):
        for j in range(n):
            print(distance[i][j], end=' ')
        print()


print(result)
