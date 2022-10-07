from collections import deque


def bfs(x, y, visited, board, dx, dy):
    q = deque()
    visited[x][y] = 1
    q.append(x, y, 5)
    board[x][y] += 5
    while q:
        x, y, c = q.popleft()
        if c == 0:
            break
        for i in range(3):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 < ny < m and visited[nx][ny] == 0:
                board[nx][ny] += c-1
                q.append((nx, ny))
                visited[nx][ny] = 1


def radiate(board, x, y, d):
    # 오른쪽
    visited = [[0]*(m) for i in range(n)]
    if d == 1:
        dx = [-1, 0, 1]
        dy = [1, 1, 1]
        if 0 <= y+1 < m:
            bfs(x, y+1, visited, board, dx, dy)

    # 왼쪽
    elif d == 2:
        dx = [-1, 0, 1]
        dy = [-1, -1, -1]
        if 0 <= y-1 < m:
            bfs(x, y-1, visited, board, dx, dy)
    # 위쪽
    elif d == 3:
        dx = [-1, -1, -1]
        dx = [-1, 0, 1]
        if 0 <= x-1 < m:
            bfs(x-1, y, visited, board, dx, dy)
    # 아래쪽
    elif d == 4:
        dx = [1, 1, 1]
        dx = [-1, 0, 1]
        if 0 <= x+1 < m:
            bfs(x+1, y, visited, board, dx, dy)


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]

    dx = [-1, 0, 1]
    dy = [1, 1, 1]
    visited = [[0]*(m) for i in range(n)]
    bfs(0, 4, visited, board, dx, dy)
