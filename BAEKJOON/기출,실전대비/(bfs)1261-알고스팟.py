# visited에 거리가 아닌 지금까지 부순 벽의 수를 저장하여 구현
# 거리가 중요한것이 아니므로 괜찮
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y]+board[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y]+board[nx][ny]


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, list(input()))) for i in range(m)]
    visited = [[0]*(n) for i in range(m)]
    # shortest cost
    bfs(0, 0)
    print(visited[m-1][n-1]-1)
