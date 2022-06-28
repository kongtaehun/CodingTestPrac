import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def nextYear(board):
    new_board = [[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                count = fourDirectionCheck(board, i, j)
                temp = board[i][j] - count
                if temp < 0:
                    new_board[i][j] = 0
                else:
                    new_board[i][j] = board[i][j] - count

    return new_board


def fourDirectionCheck(board, i, j):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    count = 0
    for a in range(4):
        ni = i+dx[a]
        nj = j+dy[a]
        if 0 <= nj < m and 0 <= ni < n and board[ni][nj] == 0:
            count += 1
    return count


def countCluster(board):
    count = 0
    visited = [[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and visited[i][j] == 0:
                dfs(board, visited, i, j)
                count += 1
    return count


def dfs(board, visited, x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited[x][y] = 1
    for a in range(4):
        nx = x+dx[a]
        ny = y+dy[a]
        if 0 <= ny < m and 0 <= nx < n:
            if visited[nx][ny] == 0 and board[nx][ny] != 0:
                dfs(board, visited, nx, ny)


if __name__ == "__main__":
    n, m = map(int, input().split())

    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))

    cluster_count = 0
    result_count = 0
    while cluster_count < 2:
        board = nextYear(board)
        cluster_count = countCluster(board)
        result_count += 1
        if cluster_count == 0:
            result_count = 0
            break

    print(result_count)
