from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 확산


def cycle_up(up, board):
    # 순환방향 : 동 -> 북 -> 서 -> 남
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    x, y = up, 0
    direc = 0
    before = 0
    while True:
        nx = x+dx[direc]
        ny = y+dy[direc]
        if nx == up and ny == 0:
            break
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            direc += 1
            continue

        board[nx][ny], before = before, board[nx][ny]
        x = nx
        y = ny


def cycle_down(down, board):
    # 순환방향 : 동 -> 북 -> 서 -> 남
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y = down, 0
    direc = 0
    before = 0
    while True:
        nx = x+dx[direc]
        ny = y+dy[direc]
        if nx == down and ny == 0:
            break
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            direc += 1
            continue
        board[nx][ny], before = before, board[nx][ny]
        x = nx
        y = ny


def bfs(q, board):
    while q:
        x, y, val = q.popleft()
        if val < 5:
            continue
        cnt = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != -1:
                board[nx][ny] += val//5
                cnt += 1
        board[x][y] -= cnt*(val//5)


if __name__ == '__main__':
    n, m, t = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]

    # 공기청정기는 항상 1번열
    up = -1
    down = -1
    for i in range(n):
        if board[i][0] == -1:
            up = i
            down = i+1
            break

    for i in range(t):
        q = deque()
        for i in range(n):
            for j in range(m):
                if board[i][j] >= 5:
                    q.append((i, j, board[i][j]))
        bfs(q, board)
        cycle_up(up, board)
        cycle_down(down, board)
    print(sum(map(sum, board)) + 2)
