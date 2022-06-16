# =========config==========
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# =========method==========


def bfs(board, i, j, n, m, count):
    q = deque()
    q.append((i, j))
    board[i][j] = count
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        now = q.popleft()
        for k in range(4):
            if now[0]+dx[k] >= 0 and now[1]+dy[k] >= 0 and now[0]+dx[k] < n and now[1]+dy[k] < m and board[now[0]+dx[k]][now[1]+dy[k]] == 1:
                q.append((now[0]+dx[k], now[1]+dy[k]))
                board[now[0]+dx[k]][now[1]+dy[k]] = count


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
