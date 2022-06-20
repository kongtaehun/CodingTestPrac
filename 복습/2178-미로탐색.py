
from collections import deque


def bfs(board, x, y, n, m):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    q.append((x, y))

    while q:
        nowX, nowY = q.popleft()
        for i in range(4):
            nx = nowX+dx[i]
            ny = nowY+dy[i]
            if nx >= 0 and ny >= 0 and nx < m and ny < n:
                if board[nx][ny] == 1:
                    q.append((nx, ny))
                    board[nx][ny] = board[nowX][nowY]+1
    return board


m, n = map(int, input().split())
board = []
for i in range(m):
    board.append(list(input()))
for i in range(m):
    for j in range(n):
        board[i][j] = int(board[i][j])

print(bfs(board, 0, 0, n, m))
