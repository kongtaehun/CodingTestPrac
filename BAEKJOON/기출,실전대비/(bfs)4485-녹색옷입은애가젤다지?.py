from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(board, visited):
    q = deque()
    q.append((0, 0))
    visited[0][0] = board[0][0]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and (visited[nx][ny] == -1 or visited[nx][ny] > visited[x][y]+board[nx][ny]):
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y]+board[nx][ny]


if __name__ == '__main__':
    n = 1
    result = []
    while True:
        n = int(input())
        if n == 0:
            break
        board = [list(map(int, input().split())) for i in range(n)]
        costs = [[-1]*n for i in range(n)]
        bfs(board, costs)
        result.append(costs[-1][-1])
    for i, v in enumerate(result):
        print("Problem "+str(i+1)+": "+str(v))
