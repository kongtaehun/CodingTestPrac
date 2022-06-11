from collections import deque
# 입력
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


# BFS함수정의
def bfs(x, y):
    #   상 화 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # que를 정의하고 요소로 첫번쨰(0,0)현재위치를 넣음
    que = deque([[x, y]])
    while que:
        # que에 있는 위치에서 마지막을 뺴고
        # 이 위치와 연결된 상하좌우를 que에 삽입
        x, y = que.popleft()
        # 현재 위치에서 4방향 확인
        for i in range(4):

            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                que.append([nx, ny])

                graph[nx][ny] = graph[x][y]+1
    return graph[n-1][m-1]


print(bfs(0, 0))
for i in range(n):
    print(graph[i])
