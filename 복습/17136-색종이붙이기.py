color_paper = [0, 5, 5, 5, 5, 5]

answer = int(1e9)


def bt(board, x, y):
    global color_paper, answer
    if x >= 10:
        result = 0
        for i in range(1, 6):
            result += (5 - color_paper[i])
        answer = min(answer, result)

        return
    if y >= 10:
        bt(board, x+1, 0)
        return
    if board[x][y] == 0:
        bt(board, x, y+1)
    else:
        k = check(board, x, y)
        for kk in range(1, k+1):
            if color_paper[kk] > 0:
                for i in range(kk):
                    for j in range(kk):
                        board[x+i][y+j] = 0
                color_paper[kk] -= 1
                bt(board, x, y+kk)
                for i in range(kk):
                    for j in range(kk):
                        board[x+i][y+j] = 1
                color_paper[kk] += 1


def check(board, x, y):
    for k in range(1, 6):
        for i in range(k):
            for j in range(k):
                if x+i >= 10 or y+j >= 10 or board[x+i][y+j] == 0:
                    return k-1
    return k


def solution():
    global answer
    board = [list(map(int, input().split())) for i in range(10)]
    bt(board, 0, 0)
    if answer == int(1e9):
        print(-1)
    else:
        print(answer)


solution()
