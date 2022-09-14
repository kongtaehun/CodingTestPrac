from collections import deque
INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(board, costs, x, y):
    q = deque()
    q.append((x, y))
    costs[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if costs[nx][ny] == 0 or costs[nx][ny] > costs[x][y]+board[nx][ny]:
                    q.append((nx, ny))
                    costs[nx][ny] = costs[x][y]+board[nx][ny]


if __name__ == '__main__':
    n = int(input())
    costs = [[INF]*(n) for i in range(n)]
    board = [list(map(int, list(input()))) for i in range(n)]
    for i in range(n):
        for j in range(n):
            board[i][j] = abs(board[i][j]-1)
    bfs(board, costs, 0, 0)

    print(costs[-1][-1]-1)
