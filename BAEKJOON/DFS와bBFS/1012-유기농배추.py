# =========config==========
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# =========method==========


def dfs(board, i, j, n, m, count):
    board[i][j] = count
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    for k in range(4):
        if i+dx[k] >= 0 and j+dy[k] >= 0 and i+dx[k] < n and j+dy[k] < m and board[i+dx[k]][j+dy[k]] == 1:
            dfs(board, i+dx[k], j+dy[k], n, m, count)


def findClusterCount(board, n, m):
    count = 2
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                dfs(board, i, j, n, m, count)
                count += 1
    return count, board
# =========main==========


result = []
test = int(input())
for i in range(test):
    m, n, c = map(int, input().split())
    board = [[0]*m for i in range(n)]
    for i in range(c):
        a, b = map(int, input().split())
        board[b][a] = 1
    count, board = findClusterCount(board, n, m)

    # for i in range(n):
    #     for j in range(m):
    #         print(board[i][j], end=' ')
    #     print()
    result.append(count - 2)

for i in result:
    print(i)
