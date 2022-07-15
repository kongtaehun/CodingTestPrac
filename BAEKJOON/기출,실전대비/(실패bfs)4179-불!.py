from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def printArr(board):
    print("===============")
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=' ')
        print()
    print("===============")


def bfs(visited, board, q):

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if visited[nx][ny] == 0 and board[nx][ny] != '#':
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y]+1
        # printArr(visited)


def bfs_k(visited, f_visited, board, q):

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx >= r or nx < 0 or ny >= c or ny < 0:
                return visited[x][y]+1
            if 0 <= nx < r and 0 <= ny < c:
                if visited[nx][ny] == 0 and (board[nx][ny] != '#') and f_visited[nx][ny] > visited[x][y]+1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y]+1

    return 'IMPOSSIBLE'


if __name__ == '__main__':
    r, c = map(int, input().split())
    board = [list(map(str, list(input()))) for i in range(r)]

    # 1은 지훈 2는 불
    f_visited = [[0]*(c) for i in range(r)]
    j_visited = [[0]*(c) for i in range(r)]
    f_q = deque()
    j_q = deque()
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'F':
                f_q.append((i, j))
            elif board[i][j] == 'J':
                j_q.append((i, j))

    bfs(f_visited, board, f_q)
    print(bfs_k(j_visited, f_visited, board, j_q))
