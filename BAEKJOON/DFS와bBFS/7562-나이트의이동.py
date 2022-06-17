from collections import deque
t = int(input())
#x=n, y=m
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]


def bfs(sx, sy, board, l):
    q = deque()
    q.append((sx, sy))
    board[sx][sy] = 1
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx >= 0 and ny >= 0 and nx < l and ny < l and board[nx][ny] == 0:
                q.append((nx, ny))
                board[nx][ny] = board[x][y] + 1


for i in range(t):
    l = int(input())
    startX, startY = map(int, input().split())
    wantX, wantY = map(int, input().split())
    board = [[0]*l for i in range(l)]
    bfs(startX, startY, board, l)
    print(board[wantX][wantY]-1)
