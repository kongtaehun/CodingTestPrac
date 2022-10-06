# 기준 블록 : 무지개블록이 아닌 블록 중
# 무지개블록만 있는 그룹은 없다
from collections import deque


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 크기가 가장 큰 블록그룹찾기(무지개블록수, 기준블록고려)


def findBlock(board):
    candidate = []
    for i in range(n):
        for j in range(n):
            if board[i][j] != -1 and board[i][j] != -2:
                visited = [[0]*n for i in range(n)]
                size, rainbow, mainblock, norm = bfs(visited, board, i, j)
                if norm == False:
                    continue
                if size <= 1:
                    continue
                candidate.append((size, rainbow, mainblock, i, j))
    candidate.sort(key=lambda x: (-x[0], -x[1], -x[2][0], -x[2][1]))
    # print(candidate)
    if candidate:
        return candidate[0][0], candidate[0][3], candidate[0][4]
    else:
        return -1, -1, -1


def bfs(visited, board, x, y):
    color = board[x][y]
    q = deque()
    visited[x][y] = 1
    q.append((x, y))
    size, rainbow, mainblock, normalBlock = 1, 0, [x, y], False
    if color != 0:
        normalBlock = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and (board[nx][ny] == color or board[nx][ny] == 0):
                    if board[nx][ny] != 0:
                        normalBlock = True
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    size += 1

                    if board[nx][ny] == 0:
                        rainbow += 1
                    if board[nx][ny] != 0:
                        if mainblock[0] > nx or (mainblock[0] == nx and mainblock[1] < ny):
                            mainblock[0] = nx
                            mainblock[1] = ny
    return size, rainbow, mainblock, normalBlock


def removeBlock(x, y):
    color = board[x][y]
    visited = [[0]*n for i in range(n)]
    q = deque()
    visited[x][y] = 1
    q.append((x, y))
    board[x][y] = -2
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and (board[nx][ny] == color or board[nx][ny] == 0):
                    board[nx][ny] = -2
                    visited[nx][ny] = 1
                    q.append((nx, ny))


def printB(board):
    for i in range(n):
        for j in range(n):
            if board[i][j] == -2:
                print(' ', end=' ')
            else:
                print(board[i][j], end=' ')
        print()


def gravity(board):
    # -2는 이동할 수 있는 빈칸이라는 뜻
    temp_board = []
    board = list(map(list, zip(*board[::-1])))
    for i in range(n):
        temp_line = [-2]*(n)
        stk = []
        start = 0
        for j in range(n):
            if board[i][j] != -2 and board[i][j] != -1:
                stk.append(board[i][j])
            if board[i][j] == -1:
                for k in range(len(stk)):
                    temp_line[start+k] = stk[k]
                temp_line[j] = -1
                start = j+1
                stk = []

        for k in range(len(stk)):
            temp_line[start+k] = stk[k]

        temp_board.append(temp_line)

    temp_board = list(map(list, zip(*temp_board)))[::-1]

    return temp_board


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]
    answer = 0
    while True:
        size, x, y = findBlock(board)
        if size == -1:
            break
        answer += size**2
        removeBlock(x, y)
        board = gravity(board)
        board = list(map(list, zip(*board)))[::-1]
        board = gravity(board)
        # printB(board)
    print(answer)
