from collections import deque
# ======== input ========
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
m, n, k = map(int, input().split())
board = [[] for i in range(k)]
for i in range(k):
    for j in range(n):
        board[i].append(list(map(int, input().split())))


q = deque()

# z,x,y
for z in range(k):
    for x in range(n):
        for y in range(m):
            if board[z][x][y] == 1:
                q.append((z, x, y))

while q:
    z, x, y = q.popleft()

    for i in range(6):
        nx = x+dx[i]
        ny = y+dy[i]
        nz = z+dz[i]
        if nx >= 0 and ny >= 0 and nz >= 0 and nx < n and ny < m and nz < k and board[nz][nx][ny] == 0:
            q.append((nz, nx, ny))
            board[nz][nx][ny] = board[z][x][y]+1


maxval = 0
for z in range(k):
    for x in range(n):
        for y in range(m):
            if board[z][x][y] == 0:
                print(-1)
                exit(0)
            maxval = max(maxval,board[z][x][y])

print(maxval-1)
