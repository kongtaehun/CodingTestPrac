from copy import deepcopy
# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
# 이동, 원상복귀 함수(맨처음은 가만히)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
# 하나하나 테스트하면서 개발?


def printB(board):
    for i in board:
        print(i)
    print("sdfdfdfdfdfdf")


def bt(x, y, d, cnt):
    global ans, fishs, board
    fishMove(fishs, board)
    while True:
        nx = x+dx[d]
        ny = y + dx[d]
        if not 0 <= nx < 4 or not 0 <= ny < 4:
            ans = max(ans, cnt)
            return
        if not board[nx][ny]:
            x, y = nx, ny
            continue

        org_board, org_fishs = deepcopy(board), deepcopy(fishs)
        bt(nx, ny, fishs[board[nx][ny]][2], board[nx][ny])
        board, fishs = org_board, org_fishs
        x, y = nx, ny


def fishMove(fishs, board):
    # 물고기 이동
    for j in range(1, 17):
        x, y, d = fishs[j]
        if x == -1:
            continue
        for i in range(8):
            nx = x+dx[(d+i) % 8]
            ny = y+dy[(d+i) % 8]
            if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny] != -1:
                fishs[j][2] = (d+i) % 8
                fishs[board[nx][ny]] = [x, y, fishs[board[nx][ny]][2]]
                fishs[j] = [nx, ny, fishs[j][2]]
                board[x][y] = board[nx][ny]
                board[nx][ny] = j
                break


def sharkMove(board, shark):
    x, y, d = shark
    while 0 <= x < 4 and 0 <= y < 4:
        x = x+dx[d]
        y = y+dy[d]


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
    ans = result
    bt(0, 0, fishs[board[0][0]][2], result)
    print(ans)
