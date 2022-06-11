import time
# 코드 실행시간 2.4초 시간초과


n, m = list(map(int, input().split()))
x, y, d = list(map(int, input().split()))
board = []
for i in range(n):
    temp = list(map(int, input().split()))
    board.append(temp)

#  0
# 3x1
#  2

#    x-1
# y-1   y+1
#    x+1
# 이동한 곳은 2로 표사
start_time = time.time()
board[x][y] = 2
while True:
    if board[x][y-1] != 0 and board[x][y+1] != 0 and board[x+1][y] != 0 and board[x-1][y] != 0:
        if d == 0:
            if board[x+1][y] == 1:
                break
            else:
                x = x+1
        elif d == 3:
            if board[x+1][y] == 1:
                break
            else:
                y = y+1

        elif d == 2:
            if board[x+1][y] == 1:
                break
            else:
                x = x-1
        elif d == 1:
            if board[x+1][y] == 1:
                break
            else:
                y = y-1

    if d == 0:
        if board[x][y-1] == 0:
            y = y-1
            board[x][y] = 2
            d = 3
        else:
            d = 3
    elif d == 3:
        if board[x+1][y] == 0:
            x = x+1
            board[x][y] = 2
            d = 2
        else:
            d = 2
    elif d == 2:
        if board[x][y+1] == 0:
            y = y+1
            board[x][y] = 2
            d = 1
        else:
            d = 1
    elif d == 1:
        if board[x-1][y] == 0:
            x = x-1
            board[x][y] = 2
            d = 0
        else:
            d = 0
print(sum(board, []).count(2))
end_time = time.time()
print(end_time-start_time)
