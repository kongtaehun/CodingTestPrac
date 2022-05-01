# 연결된 총개수?
# 입력
n = 6
m = 6
# 2차원 dp테이블 초기ㅗ하
INF = 1e9
graph = [[INF]*(n+1) for i in range(n+1)]

# 자기자신 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 링크정보입력
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 플루이드 워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print('X', end=' ')
        else:
            print(graph[i][j], end=' ')
    print()


# 4에서 다른 모든점, 반대로도 합해서 n-1개
result_count = 0
for k in range(1, n+1):
    count = 0
    for i in range(1, n+1):
        if i != k:
            if graph[k][i] != INF:
                count += 1  # inf가 아닌거의 개수-1
            if graph[i][k] != INF:
                count += 1

    if count == 5:
        result_count += 1

print(result_count)
