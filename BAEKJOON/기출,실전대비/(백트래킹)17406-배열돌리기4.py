from copy import deepcopy
# a~b범위 c~d범위까지의 배열의 겉테두리를 회전한다.
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

answer = int(1e9)


def bt(depth, k, visited, result, board, rotate_inf):
    global answer
    if depth == k:
        temp_board = deepcopy(board)
        for i in result:
            a, b, c = rotate_inf[i]
            for s in range(1, c+1):
                rotate(temp_board, a, b, s)
        answer = min(boardGrade(temp_board), answer)

    else:
        for i in range(k):
            if visited[i] == 0:
                visited[i] = 1
                result.append(i)
                bt(depth+1, k, visited, result, board, rotate_inf)
                visited[i] = 0
                result.pop()


def copy_board(origin, board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = origin[i][j]


def printB(board):
    for i in board:
        print(i)


def boardGrade(board):
    min_result = int(1e9)
    for i in board:
        min_result = min(sum(i), min_result)
    return min_result


def rotate(board, r, c, s):
    x = r-s
    y = c-s
    d = 0
    now = board[x][y]
    while True:
        # 한칸이동
        x = x+dx[d]
        y = y+dy[d]
        if x > r+s or y > c+s or x < r-s or y < c-s:  # 범위넘어갔을 경우
            x = x-dx[d]  # 뒤로한칸이동하고
            y = y-dy[d]
            d += 1  # 방향바꾸고
            x = x+dx[d]  # 다시이동
            y = y+dy[d]
        board[x][y], now = now, board[x][y]

        if x == r-s and y == c-s:
            break


def solution():
    global answer
    n, m, k = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]
    rotate_inf = []
    for i in range(k):
        a, b, c = map(int, input().split())
        rotate_inf.append((a-1, b-1, c))
    result = []
    visited = [0]*(k)
    bt(0, k, visited, result, board, rotate_inf)
    print(answer)


solution()
