
# 가로선들을 넣는 함수(가로선들이 연속되면 안된다.)
def bt(depth):
    global flag
    if gameStart(board):
        flag = min(depth, flag)
        return
    elif depth == 3 or flag <= depth:
        return

    else:
        for i in range(1, n):
            for j in range(1, m+1):
                if board[j][i] == 0 and board[j][i+1] == 0:
                    board[j][i+1] = i
                    board[j][i] = i+1
                    bt(depth+1)
                    board[j][i+1] = 0
                    board[j][i] = 0


# 사다리 게임을 하는 함수
def gameStart(board):
    temp = []
    for now in range(1, n+1):
        origin_now = now
        for j in range(1, m+1):
            # i번째 세로선에서 j번째 가로선
            if board[j][now] != 0 and (board[j][now] == now+1 or board[j][now] == now-1):
                now = board[j][now]
        if now != origin_now:
            return False
    return True


if __name__ == '__main__':
    n, h, m = map(int, input().split())
    board = [[0]*(n+1) for i in range(m+1)]
    for i in range(h):
        a, b = map(int, input().split())
        board[a][b] = b+1
        board[a][b+1] = b
    if m == 0:
        print(0)
        exit(0)
    flag = 4
    bt(0)
    print(-1 if flag == 4 else flag)

# def printBoard(board):
#     for i in range(1, m+1):
#         for j in range(1, n+1):
#             print(board[i][j], end=' ')
#         print()
