from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y, visited, color):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if visited[nx][ny] == 0 and board[nx][ny] == color:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    count += 1
    return count


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = []
    result_B = 0
    result_W = 0
    for i in range(m):
        temp = input()
        temp = list(temp)
        board.append(temp)
    visited = [[0]*(n) for i in range(m)]
    for i in range(m):
        for j in range(n):
            if visited[i][j] == 0:
                count = bfs(i, j, visited, board[i][j])

                if board[i][j] == 'W':
                    result_W += count*count
                elif board[i][j] == 'B':
                    result_B += count*count

    print(result_W, result_B)
