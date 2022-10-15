
from copy import deepcopy


dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
ddx = [-1, 0, 1, 0]
ddy = [0, -1, 0, 1]
shark_board = [[0]*4 for i in range(4)]
fish_board = [[[] for i in range(4)] for i in range(4)]
smell_board = [[0]*4 for i in range(4)]


def printB(board):
    for i in board:
        print(i)


def fish_move():
    temp_board = [[[] for i in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            if fish_board[i][j]:
                for k in range(len(fish_board[i][j])):
                    d = fish_board[i][j][k]
                    flag = 0
                    # 방향바꾸기
                    for _ in range(8):
                        if 0 > i+dx[d] or i+dx[d] >= 4 or 0 > j+dy[d] or j+dy[d] >= 4 or smell_board[i+dx[d]][j+dy[d]] != 0 or shark_board[i+dx[d]][j+dy[d]] == 1:
                            d -= 1
                            if d == -1:
                                d = 7
                        else:
                            flag = 1
                            break
                    if flag == 1:
                        temp_board[i+dx[d]][j+dy[d]].append(d)
                    else:
                        temp_board[i][j].append(fish_board[i][j][k])
    return temp_board, fish_board


result = []
poss_dirc = []


def bt(depth, x, y):
    global result, poss_dirc
    if depth == 3:
        poss_dirc.append(deepcopy(result))
    else:
        for i in range(4):
            nx = x + ddx[i]
            ny = y + ddy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                result.append(i)
                bt(depth+1, nx, ny)
                result.pop()


def findSharkMove(a, b):
    global poss_dirc, result
    # 0246
    # 좌상우하
    poss_dirc = []
    result = []

    bt(0, a, b)
    poss_dirc.sort()

    # 이동하는 길에 있는 물고기의 수
    origin_a = a
    origin_b = b
    fish_cnt = [0]*(len(poss_dirc))

    for idx, d in enumerate(poss_dirc):
        a = origin_a
        b = origin_b
        visited = [[0]*4 for i in range(4)]

        for i in d:
            a = a+ddx[i]
            b = b+ddy[i]
            if fish_board[a][b] and visited[a][b] == 0:
                fish_cnt[idx] += len(fish_board[a][b])
                visited[a][b] = 1
    a = origin_a
    b = origin_b
    # mx값을 가진 가장 작은 인덱스

    mx = max(fish_cnt)
    idx = 0
    for i in range(len(fish_cnt)):
        if fish_cnt[i] == mx:
            idx = i
            break
    # 상어 이동하면서 물고기 물리치기

    a, b = sharkMove(poss_dirc[idx], a, b)

    return a, b


def sharkMove(shark_moves, a, b):
    shark_board[a][b] = 0
    for i in shark_moves:
        a = a + ddx[i]
        b = b + ddy[i]
        if fish_board[a][b]:
            smell_board[a][b] = 3
            fish_board[a][b] = []
    shark_board[a][b] = 1
    return a, b


def recalSmell():
    global smell_board
    for i in range(4):
        for j in range(4):
            if smell_board[i][j] >= 1:
                smell_board[i][j] -= 1


def duplicateFish(origin_board):
    global fish_board
    for i in range(4):
        for j in range(4):
            if origin_board[i][j]:
                for f in origin_board[i][j]:
                    fish_board[i][j].append(f)


def checkFishs():
    global fish_board
    result = 0
    for i in range(4):
        for j in range(4):
            if fish_board:
                result += len(fish_board[i][j])
    return result


def solution():
    global result, poss_dirc, fish_board, shark_board, smell_board
    m, s = map(int, input().split())
    for _ in range(m):
        x, y, d = map(int, input().split())
        fish_board[x-1][y-1].append(d-1)
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    shark_board[a][b] = 1
    for i in range(s):
        temp_board, fish_board = fish_move()
        origin_board = deepcopy(fish_board)
        fish_board = temp_board
        a, b = findSharkMove(a, b)
        recalSmell()
        duplicateFish(origin_board)
        # printB(fish_board)
        # print()
        # printB(shark_board)
        # print()
        # printB(smell_board)
        # print('--------------')
    print(checkFishs())
    # printB(shark_board)
    # print()
    # printB(fish_board)
    # print()
    # printB(smell_board)


solution()
