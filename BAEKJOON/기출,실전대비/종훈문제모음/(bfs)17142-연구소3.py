from collections import deque
from itertools import combinations
import copy
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
INF = int(1e9)
# 백트래킹


def com(candidate, m, board, walls):
    global answer
    for cand in list(combinations(candidate, m)):

        q = deque()
        for x, y in cand:
            q.append((x, y, 0))
        visited = [[0]*(n) for i in range(n)]
        for x, y in walls:
            visited[x][y] = 1
        for x, y in candidate:
            visited[x][y] = -1

        temp = bfs(q, visited, board)

        answer = min(temp, answer)


# visited -> 벽1, 선택안된비활성1
def bfs(q, visited, board):
    if initcheck(visited):
        return 0
    while q:
        x, y, step = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if (board[nx][ny] == 0 or board[nx][ny] == 2) and (visited[nx][ny] == 0 or visited[nx][ny] == -1):
                    visited[nx][ny] = step+1
                    q.append((nx, ny, step+1))
    return check(visited, step)


def initcheck(visited):
    for i in visited:
        for j in i:
            if j == 0:
                return False
    return True


def check(visited, step):
    # step이 바이러스의 자리이면

    for i in visited:
        for j in i:
            if j == 0:
                return INF

    flag = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                visited[i][j] = 0

    mx = max(map(max, visited))

    return mx


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]
    walls = []
    visited = [[0]*(n) for i in range(n)]
    candidate = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                candidate.append((i, j))
            elif board[i][j] == 1:
                walls.append((i, j))

    q = deque()
    answer = INF
    com(candidate, m, board, walls)
    if answer == INF:
        print(-1)
    else:
        print(answer)
