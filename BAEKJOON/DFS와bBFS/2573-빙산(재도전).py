from collections import deque
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def countCluster(board):
    visited = [[0]*m for i in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and board[i][j] != 0:
                meltq = bfs(visited, board, i, j)
                count += 1
                while meltq:
                    x, y, melt = meltq.popleft()
                    board[x][y] = max(board[x][y] - melt, 0)
    return count, board


def bfs(visited, board, x, y):
    q = deque()
    q.append((x, y))
    meltq = deque()
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        meltcount = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if board[nx][ny] != 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                else:
                    meltcount += 1
        # 이거 최적화
        if meltcount:
            meltq.append((x, y, meltcount))
    return meltq


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))
    count = 0
    result = 0
    while count < 2:

        count, board = countCluster(board)
        if count == 0:
            result = 1
            break
        result += 1
    print(result-1)
