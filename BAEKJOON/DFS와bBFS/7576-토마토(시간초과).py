#for문으로 순회하며 1을 찾을 때마다 bfs를 실행하였다
# 시간초과!!!!

from collections import deque
# ========input==========
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
board = []
for i in range(m):
    board.append(list(map(int, input().split())))
# ========method==========


def getResult(board):
    for i in range(m):
        for j in range(n):
            if board[i][j] == 0:
                return -1
    return max(max(board))-1


def bfs(x, y, board, n, m):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx >= 0 and ny >= 0 and nx < m and ny < n and board[nx][ny] != -1:
                if board[nx][ny] == 0 or board[nx][ny] > board[x][y]+1:
                    board[nx][ny] = board[x][y]+1
                    q.append((nx, ny))


# =======main============
# 저장될떄부터 모든 토마토가 익어있는상태 예외
zero_count = 0
flat_list = set(sum(board, []))
if 0 not in flat_list:
    print(0)
else:
    for i in range(m):
        for j in range(n):
            if board[i][j] == 1:
                bfs(i, j, board, n, m)

    print(getResult(board))
