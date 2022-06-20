# 벽을 부쉈을 떄 visited와  아닐떄의 visited를 분류해야한다.

from collections import deque
n, m = map(int, input().split())
board = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for i in range(n):
    board.append(list(map(int, list(input()))))
visited = [[[0]*2 for i in range(m)] for i in range(n)]

q = deque()
q.append((0, 0, 0))
# 2부터 시작했다
visited[0][0][0] = 2
while q:
    x, y, z = q.popleft()
    if x == n-1 and y == m-1:
        break
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if board[nx][ny] == 0 and visited[nx][ny][z] == 0:
                q.append((nx, ny, z))
                visited[nx][ny][z] = visited[x][y][z]+1
            elif board[nx][ny] == 1 and z == 0:
                q.append((nx, ny, z+1))
                # 부쉈을 떄 결과를 z축하나늘려서 저장하고
                # q에 z+1을 입력한다.
                visited[nx][ny][z+1] = visited[x][y][z]+1

if sum(visited[n-1][m-1]) == 0:
    print(-1)
else:

    print(visited[x][y][z]-1)
