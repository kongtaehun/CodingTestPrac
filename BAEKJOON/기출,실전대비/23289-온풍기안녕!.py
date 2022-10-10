from collections import deque
from copy import deepcopy


def printB(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=' ')
        print()


def bfs(x, y, visited, board, dx, dy, walls, not_include):
    q = deque()
    visited[x][y] = 1
    q.append((x, y, 5))
    board[x][y] += 5

    while q:
        x, y, c = q.popleft()
        if c == 0:
            break
        for i in range(3):

            nx = x+dx[i]
            ny = y+dy[i]

            flag = True
            for j in not_include[i]:
                print(x+j[0], y+j[1], x+j[2], y+j[3])
                if (x+j[0], y+j[1], x+j[2], y+j[3]) in walls:
                    flag = False
                    break
            if flag == False:
                continue

            if 0 <= nx < n and 0 < ny < m and visited[nx][ny] == 0:
                board[nx][ny] += c-1
                q.append((nx, ny, c-1))
                visited[nx][ny] = 1


def radiate(board, x, y, d, walls):
    # 오른쪽
    visited = [[0]*(m) for i in range(n)]
    if d == 1:
        dx = [-1, 0, 1]
        dy = [1, 1, 1]
        not_include_wall = [[(0, 0, -1, 0), (-1, 0, -1, 1)],
                            [(0, 0, 0, 1)], [(0, 0, 1, 0), (1, 0, 1, 1)]]
        if 0 <= y+1 < m:
            bfs(x, y+1, visited, board, dx, dy, walls, not_include_wall)

    # 왼쪽
    elif d == 2:
        dx = [-1, 0, 1]
        dy = [-1, -1, -1]
        not_include_wall = [[(0, 0, -1, 0), (-1, 0, -1, -1)],
                            [(0, 0, 0, -1)], [(0, 0, 1, 0), (1, 0, 1, -1)]]
        if 0 <= y-1 < m:
            bfs(x, y-1, visited, board, dx, dy, walls, not_include_wall)
    # 위쪽
    elif d == 3:
        dx = [-1, -1, -1]
        dy = [-1, 0, 1]
        not_include_wall = [[(0, 0, 0, -1), (0, -1, -1, -1)],
                            [(0, 0, -1, 0)], [(0, 0, 0, 1), (0, 1, -1, 1)]]
        if 0 <= x-1 < m:
            bfs(x-1, y, visited, board, dx, dy, walls, not_include_wall)
    # 아래쪽
    elif d == 4:
        dx = [1, 1, 1]
        dy = [-1, 0, 1]
        not_include_wall = [[(0, 0, 0, -1), (0, -1, 1, -1)],
                            [(0, 0, 1, 0)], [(0, 0, 0, 1), (0, 1, 1, 1)]]
        if 0 <= x+1 < m:
            bfs(x+1, y, visited, board, dx, dy, walls, not_include_wall)


def controlTemp(board, wall):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    temp_board = deepcopy(board)
    for i in range(n):
        for j in range(m):
            for d in range(4):
                if (i, j, i+dx[d], j+dy[d]) not in wall:
                    if board[i][j] > board[i+dx[d]][j+dy[d]]:
                        temp_board[i+dx[d]][j+dy[d]
                                            ] += abs(board[i][j] - board[i+dx[d]][j+dy[d]])//4
                        temp_board[i][j] -= abs(board[i]
                                                [j] - board[i+dx[d]][j+dy[d]])//4
                    # 벽고려


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]
    w = int(input())
    wall = set()
    for i in range(w):
        x, y, t = map(int, input().split())
        if t == 0:
            wall.add((x-1, y-1, x-2, y-1))
            wall.add((x-2, y-1, x-1, y-1))
        elif t == 1:
            wall.add((x-1, y-1, x-1, y))
            wall.add((x-1, y, x-1, y-1))
