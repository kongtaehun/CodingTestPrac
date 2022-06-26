import sys
sys.setrecursionlimit(10 ** 8)


def printArr(board):
    print("================")

    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=' ')
        print()
    print("================")


def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    ways = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < n and ny < m and nx >= 0 and ny >= 0:
            if board[x][y] > board[nx][ny]:
                ways += dfs(nx, ny)
    dp[x][y] = ways
    return dp[x][y]


n, m = map(int, input().split())
board = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    board.append(list(map(int, input().split())))
dp = [[-1]*m for i in range(n)]


print(dfs(0, 0))
