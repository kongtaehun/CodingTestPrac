from copy import deepcopy
# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
# 이동, 원상복귀 함수(맨처음은 가만히)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
# 하나하나 테스트하면서 개발?


def printB(board):
    for i in board:
        print(i)


def fishMove(fishs, board):
    # 물고기 이동
    for j in range(1, 17):
        x, y, d = fishs[j]
        if x == -1 or y == -1 or board[x][y] == -1:
            continue
        for i in range(8):
            nx = x+dx[(d+i) % 8]
            ny = y+dy[(d+i) % 8]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if board[nx][ny] == -1:
                    continue
                else:
                    fishs[j][2] = (d+i) % 8
                    fishs[board[nx][ny]] = [x, y, fishs[board[nx][ny]][2]]
                    fishs[j] = [nx, ny, fishs[j][2]]
                    board[x][y] = board[nx][ny]
                    board[nx][ny] = j
                    break


def getPossiblePos(x, y, d):

    pos = []
    x = x+dx[d]
    y = y+dy[d]
    while 0 <= x < 4 and 0 <= y < 4:
        # print(x, y)
        if board[x][y] == 0 or board[x][y] == -1:
            x = x+dx[d]
            y = y+dy[d]
            continue
        else:
            pos.append((x, y))
        x = x+dx[d]
        y = y+dy[d]
    return pos


def bt(depth, x, y, d):

    global answer, result, fishs, board
    fishMove(fishs, board)
    pos = getPossiblePos(x, y, d)

    if len(pos) == 0:
        answer = max(result, answer)
        return
    for i in range(len(pos)):

        nx, ny = pos[i]
        origin_board, origin_fishs = deepcopy(board), deepcopy(fishs)
        if board[x][y] != 0:
            d = fishs[board[nx][ny]][2]
        board[x][y] = 0
        cost = board[nx][ny]
        result += cost
        fishs[board[nx][ny]][0] = -1
        board[nx][ny] = -1
        bt(depth+1, nx, ny, d)

        board, fishs = origin_board, origin_fishs
        result -= cost


if __name__ == '__main__':
    # 현재 물고기들의 인덱스(x,y,방향) , -1이면 먹힌거
    fishs = [[0, 0, 0]]*17
    board = [[0]*4 for i in range(4)]
    temp = [list(map(int, input().split())) for i in range(4)]
    for i in range(4):
        fishs[temp[i][0]] = [i, 0, temp[i][1]-1]
        board[i][0] = temp[i][0]
        fishs[temp[i][2]] = [i, 1, temp[i][3]-1]
        board[i][1] = temp[i][2]
        fishs[temp[i][4]] = [i, 2, temp[i][5]-1]
        board[i][2] = temp[i][4]
        fishs[temp[i][6]] = [i, 3, temp[i][7]-1]
        board[i][3] = temp[i][6]

    # 현재 상어의 위치
    shark = [0, 0, fishs[board[0][0]][2]]
    result = board[0][0]
    fishs[board[0][0]][0] = -1
    board[0][0] = -1
    answer = 0
    bt(0, 0, 0, shark[2])
    print(answer)
