from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, visited):
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
                    visited[nx][ny] = visited[x][y]+1
                    q.append((nx, ny))


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = []
    for i in range(n):
        temp = list(map(int, list(input())))
        board.append(temp)
    visited = [[0]*(m) for i in range(n)]
    bfs(0, 0, visited)
    print(visited[n-1][m-1])
