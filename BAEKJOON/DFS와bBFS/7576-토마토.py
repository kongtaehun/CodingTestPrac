# for문으로 순회하며 1을 찾을 때마다 bfs를 실행하였다
# 시간초과!!!!

from collections import deque
# ========method==========


def getResult(board, n, m):
    maxval = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == 0:
                return -1
        maxval = max(maxval, max(board[i]))
    return maxval-1


# ========input==========
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
board = []
for i in range(m):
    board.append(list(map(int, input().split())))


# 시작해야하는 점 큐에 한번에 다 넣기
q = deque()
for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            q.append((i, j))


# =======main============
# 저장될떄부터 모든 토마토가 익어있는상태 예외

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >= 0 and ny >= 0 and nx < m and ny < n and board[nx][ny] == 0:
            board[nx][ny] = board[x][y]+1
            q.append((nx, ny))

print(getResult(board, n, m))
