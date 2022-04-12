# n, m, k = map(int, input().split())
# graph = []
# for i in range(m):
#     graph.append(list(map(int, input())))


from collections import deque
n = 4
m = 4
k = 2
x = 1
graph = [[1, 2], [1, 3], [2, 3], [2, 4]]
graph_node = [[]for i in range(n+1)]
distance_fromone = [99 for i in range(n+1)]
# 출발지점인덱스 0으로 초기화
distance_fromone[x] = 0

for i in range(len(graph)):
    graph_node[graph[i][0]].append(graph[i][1])


# 거리가 1이므로 원래 비용과 비교하며 계산할 필요 없다(min쓸필요 없다)
q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph_node[now]:
        # 방문하지 않았다면
        if distance_fromone[next_node] == 99:
            # 현재노드와 비용 1을 더해 다음노드의 최단거리 초기화
            distance_fromone[next_node] = distance_fromone[now]+1
            q.append(next_node)

for i in range(len(distance_fromone)):
    if distance_fromone[i] == k:
        print(i)
