# 모든노드 서로가 서로에게 걸리는 최단거리 전부다 계산하기
# O(N^3)
import sys
input = sys.stdin.readline
# 무한 값 초기화
INF = int(1e9)
# 노드 개수, 간선개수 받기
n, m = map(int, input().split())
# 2차원 간선 비용 정보 받기
graph = [[INF]*(n+1) for i in range(n+1)]
# 자기자신에서 자기자신에게 가는 간선 비용 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0
# 간선에 대한 정보받고
# graph[a,][b] --> a에서 b로가는 비용
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플루이드 워셜 알고리즘
# i에서 j로갈때 k를 거쳐서 갈때
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j], end=" ")
