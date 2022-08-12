from collections import deque
from itertools import combinations
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def countSafeArea(visited, board):

    count = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and board[i][j] == 0:
                count += 1
    return count


def bfs(board, visited, birus):
    q = deque()
    for i in birus:
        q.append((i[0], i[1]))
        visited[i[0]][i[1]] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and board[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]
    walls = []
    birus = []

    # 0인 인덱스를 받아온다.
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                walls.append((i, j))
            if board[i][j] == 2:
                birus.append((i, j))
    result = 0
    for wall in list(combinations(walls, 3)):
        visited = [[0]*(m) for i in range(n)]
        board[wall[0][0]][wall[0][1]] = 1
        board[wall[1][0]][wall[1][1]] = 1
        board[wall[2][0]][wall[2][1]] = 1
        bfs(board, visited, birus)

        result = max(countSafeArea(visited, board), result)
        board[wall[0][0]][wall[0][1]] = 0
        board[wall[1][0]][wall[1][1]] = 0
        board[wall[2][0]][wall[2][1]] = 0
    print(result)
