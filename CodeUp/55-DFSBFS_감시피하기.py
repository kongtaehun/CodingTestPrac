# 입력
from itertools import combinations
from collections import deque
n = 5
board = [['x', 's', 'x', 'x', 't'], ['t', 'x', 's', 'x', 'x'], [
    'x', 'x', 'x', 'x', 'x'], ['x', 't', 'x', 'x', 'x'], ['x', 'x', 't', 'x', 'x']]

# x인곳 인덱스 찾기
x_index = []
t_index = []
s_index = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 'x':
            x_index.append([i, j])
        if board[i][j] == 't':
            t_index.append([i, j])
        if board[i][j] == 's':
            s_index.append([i, j])

# 각 인덱스들 combinations
장애물경우의수 = list(combinations(x_index, 3))


# def board의 발각여부 체크
# (x,y,이동방향정보)
def dfs(x, y, move_type, temp):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if temp[x][y] == 'o':
        return False
    elif board[x][y] == 'x' or board[x][y] == 't' or board[x][y] == 's':
        temp[x][y] = 't'
        if move_type == 'up' or move_type == 'no':
            dfs(x-1, y, 'up', temp)
        if move_type == 'down' or move_type == 'no':
            dfs(x+1, y, 'down', temp)
        if move_type == 'left' or move_type == 'no':
            dfs(x, y-1, 'left', temp)
        if move_type == 'right' or move_type == 'no':
            dfs(x, y+1, 'right', temp)
        return True

    return False


def s_check(bd):
    for i in range(n):
        for j in range(n):
            if bd[i][j] == 's':
                return True
    return False


# 발각 가능한곳의 값을 변경
# 장애물 경우마다
for i in 장애물경우의수:
    temp = [['x']*(n) for _ in range(n)]
    for j in s_index:
        temp[j[0]][j[1]] = 's'
    temp[i[0][0]][i[0][1]] = 'o'
    temp[i[1][0]][i[1][1]] = 'o'
    temp[i[2][0]][i[2][1]] = 'o'
    for t in t_index:
        dfs(t[0], t[1], 'no', temp)
    if s_check(temp) == True:

        break
if s_check(temp) == True:
    print('YES')
else:
    print('NO')

for i in range(n):
    for j in range(n):
        print(temp[i][j], end=' ')
    print()
