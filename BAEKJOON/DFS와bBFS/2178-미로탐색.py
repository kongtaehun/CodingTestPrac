# ==========config=========
import sys
from collections import deque
input = sys.stdin.readline


# ==========input=========
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, input().split())
board = []
for i in range(n):
    temp = list(input()[:-1])
    board.append(temp)
for i in range(n):
    for j in range(m):
        board[i][j] = int(board[i][j])
# ==========method=========


def bfs(board, x, y):
    q = deque()
    q.append((x, y))
    board[x][y] = 1
    while q:
        now = q.popleft()
        for i in range(4):
            if now[0]+dx[i] >= 0 and now[1]+dy[i] >= 0 and now[0]+dx[i] < n and now[1]+dy[i] < m:
                if board[now[0]+dx[i]][now[1]+dy[i]] == 1:
                    q.append((now[0]+dx[i], now[1]+dy[i]))
                    board[now[0]+dx[i]][now[1]+dy[i]] = board[now[0]][now[1]]+1


# ==========main=========
bfs(board, 0, 0)
print(board[n-1][m-1])
