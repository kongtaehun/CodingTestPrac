def move(now_loc, dice, direc):
    if direc == 1:
        if 0 > (now_loc[1] + 1) or m <= (now_loc[1] + 1):
            return
        temp4 = dice[1][0]
        temp1 = dice[1][1]
        temp3 = dice[1][2]
        temp6 = dice[3][1]
        dice[1][0] = temp1
        dice[1][1] = temp3
        dice[1][2] = temp6
        dice[3][1] = temp4
        now_loc[1] += 1
        # 밑면
        if board[now_loc[0]][now_loc[1]] != 0:
            dice[3][1] = board[now_loc[0]][now_loc[1]]
            board[now_loc[0]][now_loc[1]] = 0
        else:
            board[now_loc[0]][now_loc[1]] = dice[3][1]
        print(dice[1][1])
    elif direc == 2:
        if 0 > (now_loc[1] - 1) or m <= (now_loc[1] - 1):
            return
        temp4 = dice[1][0]
        temp1 = dice[1][1]
        temp3 = dice[1][2]
        temp6 = dice[3][1]
        dice[1][0] = temp6
        dice[1][1] = temp4
        dice[1][2] = temp1
        dice[3][1] = temp3
        now_loc[1] -= 1
        # 밑면
        if board[now_loc[0]][now_loc[1]] != 0:
            dice[3][1] = board[now_loc[0]][now_loc[1]]
            board[now_loc[0]][now_loc[1]] = 0
        else:
            board[now_loc[0]][now_loc[1]] = dice[3][1]
        print(dice[1][1])
    elif direc == 4:
        if 0 > (now_loc[0] + 1) or n <= (now_loc[0] + 1):
            return
        temp2 = dice[0][1]
        temp1 = dice[1][1]
        temp5 = dice[2][1]
        temp6 = dice[3][1]
        dice[0][1] = temp6
        dice[1][1] = temp2
        dice[2][1] = temp1
        dice[3][1] = temp5
        now_loc[0] += 1
        # 밑면
        if board[now_loc[0]][now_loc[1]] != 0:
            dice[3][1] = board[now_loc[0]][now_loc[1]]
            board[now_loc[0]][now_loc[1]] = 0
        else:
            board[now_loc[0]][now_loc[1]] = dice[3][1]
        print(dice[1][1])
    elif direc == 3:
        if 0 > (now_loc[0] - 1) or n <= (now_loc[0] - 1):
            return
        temp2 = dice[0][1]
        temp1 = dice[1][1]
        temp5 = dice[2][1]
        temp6 = dice[3][1]
        dice[0][1] = temp1
        dice[1][1] = temp5
        dice[2][1] = temp6
        dice[3][1] = temp2
        now_loc[0] -= 1
        # 밑면
        if board[now_loc[0]][now_loc[1]] != 0:
            dice[3][1] = board[now_loc[0]][now_loc[1]]
            board[now_loc[0]][now_loc[1]] = 0
        else:
            board[now_loc[0]][now_loc[1]] = dice[3][1]
        print(dice[1][1])


if __name__ == '__main__':
    n, m, x, y, k = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]
    moves = list(map(int, input().split()))
    dice = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    #위쪽 > dice[1][1]
    #아래 > dice[3][1]
    now_loc = [x, y]
    for i in moves:

        move(now_loc, dice, i)
