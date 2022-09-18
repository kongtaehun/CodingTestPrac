import copy
from collections import deque
from itertools import combinations
from os import remove
dx = [0, -1, 0]
dy = [-1, 0, 1]

# 동시공격도 고려


def printArr(board):
    for i in board:
        print(i)
    print()


def bfs(board, visited, x, y, d):
    q = deque()
    q.append((x, y, 1))
    visited[x][y] = 1
    while q:
        x, y, dist = q.popleft()
        if board[x][y] == 1 and dist <= d:
            return x, y
        if dist > d:
            return -1, -1
        for i in range(3):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                q.append((nx, ny, dist+1))
                visited[nx][ny] = 1
    return -1, -1


def gameStart(board, archers, d):
    global result
    for _ in range(n):
        removeset = set()
        visited = [[0]*(m) for i in range(n)]
        a, b = bfs(board, visited, n-1, archers[0], d)
        if a != -1 and b != -1:
            removeset.add((a, b))

        visited = [[0]*(m) for i in range(n)]
        a, b = bfs(board, visited, n-1, archers[1], d)
        if a != -1 and b != -1:
            removeset.add((a, b))

        visited = [[0]*(m) for i in range(n)]
        a, b = bfs(board, visited, n-1, archers[2], d)
        if a != -1 and b != -1:
            removeset.add((a, b))
        # print(removeset)
        result += len(removeset)
        for a, b in list(removeset):
            board[a][b] = 0

        board.pop()
        board = [[0]*(m)] + board
        # print(board)


if __name__ == '__main__':
    n, m, d = map(int, input().split())

    board = [list(map(int, input().split())) for i in range(n)]
    origin_board = copy.deepcopy(board)
    archers = [i for i in range(m)]

    answer = 0
    for archer in list(combinations(archers, 3)):
        result = 0
        board = copy.deepcopy(origin_board)
        gameStart(board, archer, d)
        answer = max(result, answer)
    print(answer)
