from copy import deepcopy
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
# 위 아래 왼쪽 아른쪽


def printB(board):
    for i in board:
        print(i)
    print()


def move(board, shark):
    temp_board = deepcopy(board)
    for i in range(n):
        for j in range(n):
            if board[i][j][0] != 0:
                id = board[i][j][0]  # 상어번호
                dirc = board[i][j][1]  # 상어현재방향
                prims = shark[id][dirc]  # 방향의 우선순위
                # 향이 없는것 중에
                my_area = [0, 0, 0]
                my_flag = 0  # 나의 냄새가 나는 곳
                other_flag = 0
                for dr in prims:
                    nx = i+dx[dr]
                    ny = j+dy[dr]
                    if 0 <= nx < n and 0 <= ny < n:
                        scent_id = scent_board[nx][ny][0]
                        if scent_id == 0:
                            # 이미 다른 상어가 있을 경우
                            if temp_board[nx][ny][0] != 0:
                                if temp_board[nx][ny][0] > id:
                                    temp_board[nx][ny] = [id, dr]
                                temp_board[i][j] = [0, 0]
                            # 다른상어가 없는경우
                            else:
                                temp_board[nx][ny] = [id, dr]
                                temp_board[i][j] = [0, 0]
                            other_flag = 1
                            # print(str(i)+' '+str(j)+'에 있는 상어' + str(nx) +
                            #       ' '+str(ny)+'로이동' + '방향은'+str(dr))
                            break

                        if scent_id == id and my_flag == 0:
                            # 차선책마련
                            my_area = [nx, ny, dr]
                            my_flag = 1

                if other_flag == 0 and my_flag == 1:
                    nx, ny, dr = my_area
                    # 이미 다른 상어가 있을 경우
                    if temp_board[nx][ny][0] != 0:
                        if temp_board[nx][ny][0] > id:
                            temp_board[nx][ny] = [id, dr]
                        temp_board[i][j] = [0, 0]
                    # 다른상어가 없는경우
                    else:
                        temp_board[nx][ny] = [id, dr]
                        temp_board[i][j] = [0, 0]

    return temp_board


def setScent(board, scent_board):
    for i in range(n):
        for j in range(n):
            if scent_board[i][j][0] != 0:
                scent_board[i][j][1] -= 1
                if scent_board[i][j][1] == 0:
                    scent_board[i][j] = [0, 0]
            if board[i][j][0] != 0:
                scent_board[i][j] = [board[i][j][0], k]


def check(board):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j][0] != 0 and board[i][j][0] != 1:
                return False

    return True


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]
    scent_board = [[[0, 0] for i in range(n)] for i in range(n)]
    shark = [[] for i in range(m+1)]
    d = list(map(int, input().split()))
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                scent_board[i][j] = [board[i][j], k]
                board[i][j] = [board[i][j], d[board[i][j]-1]]

            else:
                board[i][j] = [0, 0]

    for i in range(m):
        shark[i+1].append([])
        shark[i+1].append(list(map(int, input().split())))  # 위
        shark[i+1].append(list(map(int, input().split())))  # 아래
        shark[i+1].append(list(map(int, input().split())))  # 왼쪽
        shark[i+1].append(list(map(int, input().split())))  # 오른쪽

    for i in range(1002):
        # print('=============여기부터===============')
        if check(board):
            break
        board = move(board, shark)
        setScent(board, scent_board)
        # printB(board)
        # printB(scent_board)

        # print('=============여기까지===============')
    if i > 1000:
        print(-1)
    else:
        print(i)
