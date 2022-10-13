from copy import deepcopy


def getStateList():
    x = 1
    before_x = 1
    y = 1
    before_y = 0
    state_list = []
    while True:
        state_list.append((x*y, x, y))
        if x*y >= 100:
            break
        if before_x == x:
            x += 1
        else:
            before_x = x
        if before_y == y:
            y += 1
        else:
            before_y = y
    return state_list


def convertRotateArr(n, state_list, nums):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    # 가장 가까운 2차원 배열크기 찾기
    for a, x, y in reversed(state_list):
        if n >= a:
            break

    temp = [[0]*(y+(n-a)) for i in range(x)]
    visited = [[0]*(y+(n-a)) for i in range(x)]
    # 맨 끝에서부터 채우기

    for i in range(y, y+(n-a)):
        for j in range(x-1):
            visited[j][i] = 1
    limit_x = x
    limit_y = y
    d = 0
    y = len(temp[0]) - 1
    x = len(temp)-1
    while True:
        temp[x][y] = nums.pop()
        visited[x][y] = 1
        x = x+dx[d]
        y = y+dy[d]
        if x < 0 or y < 0 or x >= len(temp) or y >= len(temp[0]) or visited[x][y] == 1:
            x = x-dx[d]
            y = y-dy[d]
            d += 1
            if d == 4:
                d = 0
            x = x+dx[d]
            y = y+dy[d]
        if len(nums) == 0:
            break
    return temp, limit_x, limit_y


def pushFish(nums, n):
    min_val = int(1e9)
    min_idx = []
    for i in range(n):

        if nums[i] < min_val:
            min_val = nums[i]
            min_idx = [i]
        elif nums[i] == min_val:
            min_idx.append(i)

    for i in min_idx:
        nums[i] += 1


def distributeFish(board):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    temp_board = [[0]*(len(board[0])) for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                for d in range(4):
                    if 0 <= i+dx[d] < len(board) and 0 <= j+dy[d] < len(board[0]) and board[i+dx[d]][j+dy[d]] != 0:
                        diff = abs(board[i][j] - board[i+dx[d]][j+dy[d]])//5
                        if diff > 0 and board[i][j] > board[i+dx[d]][j+dy[d]]:
                            temp_board[i][j] -= diff
                            temp_board[i+dx[d]][j+dy[d]] += diff
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += temp_board[i][j]


def flatten(board, x, y):
    temp_line = []
    for i in range(y):
        for j in range(x-1, -1, -1):
            temp_line.append(board[j][i])

    for i in range(y, len(board[0])):
        temp_line.append(board[-1][i])
    return temp_line


def rotate180(lines):
    mid = len(lines)//2
    temp = lines[:mid]
    lines = lines[mid:]
    temp.reverse()

    temp_board = []
    temp_board.append(temp)
    temp_board.append(lines)

    mid = mid//2
    temp_squere1 = [[], []]
    for i in range(mid):
        temp_squere1[0].append(temp_board[0][i])
        temp_squere1[1].append(temp_board[1][i])
    temp_squere1 = list(map(list, zip(*temp_squere1[::-1])))
    temp_squere1 = list(map(list, zip(*temp_squere1[::-1])))
    temp_squere2 = [[], []]
    for i in range(mid, len(temp_board[0])):
        temp_squere2[0].append(temp_board[0][i])
        temp_squere2[1].append(temp_board[1][i])
    temp_board = []
    for i in temp_squere1:
        temp_board.append(i)
    for i in temp_squere2:
        temp_board.append(i)
    distributeFish(temp_board)
    temp_line = []
    for i in range(mid):
        for j in range(len(temp_board)-1, -1, -1):
            temp_line.append(temp_board[j][i])
    return temp_line


def check(lines, k):
    if (max(lines) - min(lines)) <= k:
        return False
    else:
        return True


def solution():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    state_list = getStateList()
    flag = True
    answer = 0
    while flag:
        pushFish(nums, n)
        board, limit_x, limit_y = convertRotateArr(n, state_list, nums)
        distributeFish(board)
        lines = flatten(board, limit_x, limit_y)
        nums = rotate180(lines)
        answer += 1
        flag = check(nums, k)

        # 현재 n의정리된 배열을 반환하는 함수
    # print(nums)
    print(answer)


solution()
