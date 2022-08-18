from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 비연결성이다!
# bfs로


def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=' ')
        print()


def bfs(board, visited, x, y, target, num):
    q = deque()
    q.append((x, y))
    visited[x][y] = num
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if visited[nx][ny] == 0 and board[nx][ny] == target:
                    q.append((nx, ny))
                    visited[nx][ny] = num
                    cnt += 1
    return cnt


def setRemoveBoard(visited, num):
    global remove_cell
    for i in range(12):
        for j in range(6):
            if visited[i][j] == num:
                remove_cell[i][j] = 1


def rotateBoard(board, type):
    if type == 1:
        temp_board = [['.']*(12) for i in range(6)]
        for i in range(12):
            for j in range(6):
                temp_board[j][i] = board[i][j]
    else:
        temp_board = [['.']*(6) for i in range(12)]
        for i in range(6):
            for j in range(12):
                temp_board[j][i] = board[i][j]
    return temp_board


def boom(board, remove_cell):
    for i in range(12):
        for j in range(6):
            if remove_cell[i][j] == 1:
                board[i][j] = '.'
    board = rotateBoard(board, 1)
    for i in range(6):
        temp = []
        for j in range(12):
            if board[i][j] != '.':
                temp.append(board[i][j])

        temp2 = []
        for _ in range(12-len(temp)):
            temp2.append('.')
        board[i] = temp2+temp

    board = rotateBoard(board, -1)
    return board


if __name__ == '__main__':
    board = [list(input()) for i in range(12)]
    answer = 0
    while True:
        flag = 0
        remove_cell = [[0]*(6) for i in range(12)]
        visited = [[0]*(6) for i in range(12)]
        num = 1
        for i in range(12):
            for j in range(6):
                if board[i][j] != '.' and visited[i][j] == 0:
                    cnt = bfs(board, visited, i, j, board[i][j], num)
                    if cnt >= 4:
                        setRemoveBoard(visited, num)
                        flag = 1
                    num += 1
        if flag == 0:
            break
        else:
            answer += 1
        board = boom(board, remove_cell)
        # printBoard(board)
    print(answer)
