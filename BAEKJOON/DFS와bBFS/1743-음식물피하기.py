from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, visited):
    count = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and board[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    count += 1
    return count


if __name__ == '__main__':
    n, m, k = map(int, input().split())

    board = [[0]*(m) for i in range(n)]
    for i in range(k):
        a, b = map(int, input().split())
        board[a-1][b-1] = 1

    visited = [[0]*(m) for i in range(n)]
    counts = []
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and board[i][j] == 1:
                counts.append(bfs(i, j, visited))
    print(max(counts))
