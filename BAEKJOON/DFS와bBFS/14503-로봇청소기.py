# ==============global
from collections import deque
import sys
input = sys.stdin.readline
count = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# =============func


def bfs(board, visited, x, y, direction):
    q = deque()
    q.append((x, y, direction))
    visited[x][y] = 1
    while q:
        x, y, direction = q.popleft()
        origin_direction = direction
        for i in range(4):
            direction = (direction-1)
            if direction < 0:
                direction = 4 + direction
            nx = x+dx[direction]
            ny = y+dy[direction]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny, direction))
                break
            if i == 3:
                direction = direction - 2
                if direction < 0:
                    direction = 4 + direction
                nx = x+dx[direction]
                ny = y+dy[direction]
                if board[nx][ny] == 1:
                    return
                else:
                    q.append((nx, ny, origin_direction))


if __name__ == "__main__":
    n, m = map(int, input().split())
    x, y, direction = map(int, input().split())
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))
    visited = [[0]*m for i in range(n)]
    bfs(board, visited, x, y, direction)

    print(sum(map(sum, visited)))
