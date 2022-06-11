# 입력 도시의개수, 버스의개수(링크의 개수)
n = int(input())
m = int(input())
# 2차원 dp그래프 초기화
# 나머지는 무한으로 초기화(1e9)
INF = 1e9
graph = [[INF]*(n+1) for i in range(n+1)]
# 자기자신에서 자기자신으로가는 경우 0으로초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0
# 링크정보 입력(a도시에서 b 도시까지 비용c)
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

print(graph[3][4])


# 플루이드 워셜 알고리즘
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            # i에서 j로 가는 최소경로
            # i에서 j로 갈떄 원래 비용과 거쳐서 가는 비용을 비ㅛㄱ하여 최소값을 입력
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(int(graph[i][j]), end=' ')
    print()
