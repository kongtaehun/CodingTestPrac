from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# L에 따라 회전시키는 로직 구현
# 얼음인접개수 세서 얼음의 양 줄이기
# 덩어리 구하기


def getLump(board):
    answer = 0
    visited = [[0]*(n) for i in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and board[i][j] != 0:
                visited, cnt = bfs(board, visited, i, j)
                answer = max(cnt, answer)

    return answer


def bfs(board, visited, x, y):
    q = deque()
    visited[x][y] = 1
    q.append((x, y))
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and board[nx][ny] != 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1
    return visited, cnt


def melt(board):
    selected = []
    for i in range(n):
        for j in range(n):
            cnt = 0
            if board[i][j] != 0:
                if 0 <= j-1 < n and board[i][j-1] != 0:
                    cnt += 1
                if 0 <= i-1 < n and board[i-1][j] != 0:
                    cnt += 1
                if 0 <= j+1 < n and board[i][j+1] != 0:
                    cnt += 1
                if 0 <= i+1 < n and board[i+1][j] != 0:
                    cnt += 1
                if cnt < 3:
                    selected.append((i, j))
                    # board[i][j] -= 1
    for x, y in selected:
        board[x][y] -= 1


def rotate(l):
    l = 2**l
    temp_board = [[0]*n for i in range(n)]
    for i in range(n//l):
        x = i*l

        for j in range(n//l):
            y = j*l
            for xx in range(x, x+l):
                for yy in range(y, y+l):
                    temp_board[yy][(x+l)-xx-1] = board[xx][yy]
            # temp = [[0]*l for i in range(l)]

            # for xx in range(x, x+l):
            #     for yy in range(y, y+l):
            #         temp[xx-x][yy-y] = board[xx][yy]
            # temp = list(map(list, zip(*temp[::-1])))
            # for xx in range(x, x+l):
            #     for yy in range(y, y+l):
            #         temp_board[xx][yy] = temp[xx-x][yy-y]

    return temp_board


def printB(board):
    for i in board:
        print(i)


if __name__ == '__main__':
    n, q = map(int, input().split())
    n = 2**n
    board = [list(map(int, input().split())) for i in range(n)]
    l_series = list(map(int, input().split()))

    for l in l_series:
        board = rotate(l)
        melt(board)
    # printB(board)
    sm = sum(map(sum, board))

    print(sm)
    print(getLump(board))
