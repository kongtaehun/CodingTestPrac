# -----NOTE-----
# 모든 경로에 대해서 저장이 필요하다
# 방문했다고, 비용이더 크다고 방문을 멈추면 답을 못구함
# visited없는 bfs로 풀었다
from collections import deque
# 방향상수 0,1,2
dx = [1, 1, 1]
dy = [-1, 0, 1]
INF = int(1e9)


def bfs(x, y, visited, board):
    q = deque()
    q.append((x, y, -1, board[x][y]))
    while q:
        x, y, direc, cost = q.popleft()
        if x == n-1:
            result.append(cost)
        for i in range(3):
            direc_next = i
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and direc != direc_next:
                new_cost = cost + board[nx][ny]
                q.append((nx, ny, direc_next, new_cost))


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]
    visited = [[0]*m for i in range(n)]
    result = []
    for i in range(m):
        bfs(0, i, visited, board)
    print(min(result))
