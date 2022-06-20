from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
m, n = map(int, input().split())
board = []
q = deque()
for i in range(n):
    board.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i, j))

while q:
    nowX, nowY = q.popleft()
    for i in range(4):
        nx = nowX + dx[i]
        ny = nowY + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if board[nx][ny] == 0:
                board[nx][ny] = board[nowX][nowY] + 1
                q.append((nx, ny))
print(max(map(max, board))-1)
