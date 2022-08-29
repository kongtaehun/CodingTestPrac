from collections import deque
dx = [1, 0, 1]
dy = [0, 1, 1]
# 2분탐색적용해보면 개꿀일듯?


def binary_search(board, start, end):
    while start <= end:

        mid = (start+end)//2

        if check(board, mid):
            start = mid+1
        else:
            end = mid-1
    return start


def check(board, x):
    for i in range(n-x+1):
        for j in range(m-x+1):
            if board[i][j] == 1:
                cnt = 0
                for k in range(x):
                    if min(board[i+k][j:j+x]) == 0:
                        break
                    else:
                        cnt += 1
                if cnt == x:
                    return True
    return False


def bfs(board, visited, x, y):
    q = deque()
    q.append((x, y, 1))
    visited[x][y] = 1

    while q:
        x, y, step = q.popleft()

        for i in range(3):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0:
                    return step
                if visited[nx][ny] == 0 and board[nx][ny] == 1:
                    q.append((nx, ny, step+1))

                    visited[nx][ny] = 1
            else:
                return step

    return step


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, list(input()))) for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                board[i][j] = min(board[i][j-1], board[i-1]
                                  [j-1], board[i-1][j])+1
    print((max(map(max, board)))**2)
