from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
ddx = [-1, 1, 0, 0]
ddy = [0, 0, -1, 1]
# n에 따른 이동정보


def getOrder(n):
    now_direc = 0
    now_amount = 1
    direcOrder = []
    cnt = 0
    while cnt <= n**2:
        for _ in range(now_amount):
            direcOrder.append(now_direc)
            cnt += 1
        now_direc = (now_direc+1) % 4
        for _ in range(now_amount):
            direcOrder.append(now_direc)
            cnt += 1
        now_direc = (now_direc+1) % 4
        now_amount += 1
    direcOrder = direcOrder[:n**2-1]
    return direcOrder


def destroy(board, d, s):
    x = n//2
    y = n//2
    for _ in range(s):
        x = x+ddx[d-1]
        y = y+ddy[d-1]
        board[x][y] = 0


def move(board, direcOrder):
    new_board = [[0]*n for i in range(n)]
    x = n//2
    y = n//2
    marbles = deque()
    for d in direcOrder:
        x = x+dx[d]
        y = y+dy[d]
        if board[x][y] != 0:
            marbles.append(board[x][y])
    x = n//2
    y = n//2
    for d in direcOrder:
        x = x+dx[d]
        y = y+dy[d]
        if marbles:
            new_board[x][y] = marbles.popleft()
    return new_board


def explode(board):
    temp_lines = convertLine(board)
    if temp_lines[0] == -1:
        return [-1]
    flag = True
    while flag:
        if len(temp_lines) == 0:
            return [-1]
        temp_lines, flag = explode_line(temp_lines)
    board = setExplodedBoard(temp_lines)
    return board


def convertLine(board):
    x = n//2
    y = n//2
    temp_lines = []
    for d in direcOrder:
        x = x+dx[d]
        y = y+dy[d]
        if board[x][y] != 0:
            temp_lines.append(board[x][y])
    if len(temp_lines) == 0:
        return [-1]
    else:
        return temp_lines


def setExplodedBoard(lines):
    marbles = deque(lines)
    new_board = [[0]*n for i in range(n)]
    x = n//2
    y = n//2
    for d in direcOrder:
        x = x+dx[d]
        y = y+dy[d]
        if marbles:
            new_board[x][y] = marbles.popleft()
    return new_board


def explode_line(line):
    global answer
    flag = False
    result_line = []
    stk = [line[0]]
    for i in range(1, len(line)):

        if stk[-1] == line[i]:
            stk.append(line[i])
        else:
            if len(stk) >= 4:
                # 폭발하는거
                answer[stk[-1]] += len(stk)
                stk = [line[i]]
                flag = True
            else:
                result_line += stk
                stk = [line[i]]
    if len(stk) >= 4:
        answer[stk[-1]] += len(stk)
        flag = True
    if len(stk) < 4:
        result_line += stk
    return result_line, flag


def makeGroup(board):
    line = convertLine(board)

    group = []
    # stk방법을쓸 경우 요소가 완전히없을 경우도 고려해야함
    stk = [line[0]]
    for i in range(1, len(line)):
        if stk[-1] == line[i]:
            stk.append(line[i])
        else:
            group.append((len(stk), stk[-1]))
            stk = [line[i]]
    if stk:
        group.append((len(stk), stk[-1]))
    result = []
    for a, b in group:
        result.append(a)
        result.append(b)
    board = setExplodedBoard(result)
    return board


def printB(board):
    for i in board:
        print(i)


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]
    direcOrder = getOrder(n)
    answer = [0, 0, 0, 0]

    for _ in range(m):
        d, s = map(int, input().split())
        destroy(board, d, s)

        board = move(board, direcOrder)
        board = explode(board)
        if board[0] == -1:
            break
        board = makeGroup(board)

    print(answer[1]+2*answer[2]+3*answer[3])
