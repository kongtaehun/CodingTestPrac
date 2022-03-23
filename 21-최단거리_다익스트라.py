# 노드, 연결된 그래프가 다음과 같을 때 시작노드에서 각 노드까지 최단거리 구하기
# 노드의 개수(n), 간선의 개수(m)
# 시작노드 번호(start)
# 각 노드에 연겨로디어있는 노드에 대한 정보를 담는 리스트만들기(graph)
import sys
import heapq
# 입력 속도를 높이기 위한 input
input = sys.stdin.readline
# 무한을 의미하는 10억
INF = int(1e9)


n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF for i in range(n+1)]
# (1,2,3) 첫번쨰 노드부터 두번쨰 노드까지 비용
# 간선에 대한 정보 받기
#
for i in range(m):
    a, b, c = map(int, input().split())
    # a노드에 연결된 모든 노드정보를 튜플로 입력
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # (비용,노드)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # 거리값 갱신, 우선순위 큐 넣기
    # 빼서 연관된 노드들 비용갱신하고 큐에 삽입
    # 우선순위 큐에 데이터가 존재할때까지 만 반복
    while q:
        # q에서 현재노드가 선택됨
        dist, now = heapq.heappop(q)
        # dis가 더 크다는 것은 이미 처리되었었음(다른 노드를 돌아서 현재노드를 왔기 때문에 더 크다)
        # 이미 처리되었다면 이미 연결된 노드들의 비용을 계산했었을 것이다(예상하기론 이 조건문없어도 잘 작동할거같음)
        if distance[now] < dist:
            continue
        # 연결된 노드들의 비용을 계산하여 비교하여 더 짧은 경우에만 distance에 입력
        # 더 짧은 경우에만 해당비용을 큐에 삽입
        for i in graph[now]:
            # 비용계산- 현재노드 비용+ 연결된노드 비용
            cost = dist+i[1]
            # 연결된 노드의 distance보다 cost가 작을 떄
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n+1):
    print(distance[i])
