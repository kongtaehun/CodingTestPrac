def printB(board):
    for i in board:
        print(i)


def sortF(lis):
    nums = [[i, 0] for i in range(101)]
    for i in range(len(lis)):
        if lis[i] != 0:
            nums[lis[i]][1] += 1
    nums.sort(key=lambda x: (x[1], x[0]))
    result = []
    for i in range(1, 101):
        if nums[i][1] != 0:
            result.append(nums[i][0])
            result.append(nums[i][1])
    return result


def postProc(board):
    max_size = 0
    for i in range(len(board)):
        if len(board[i]) > 100:
            board[i] = board[:100]
        max_size = max(len(board[i]), max_size)

    for i in range(len(board)):
        temp = [0]*(max_size - len(board[i]))
        board[i] = board[i] + temp


def doR(board):
    for i in range(len(board)):
        board[i] = sortF(board[i])
    postProc(board)
    return board


def doC(board):
    # 반시계방향으로 회전해야함
    board = list(map(list, zip(*board)))[::-1]

    for i in range(len(board)):
        board[i] = sortF(board[i])
    postProc(board)
    board = list(map(list, zip(*board[::-1])))
    return board


if __name__ == '__main__':
    r, c, k = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(3)]
    answer = -1
    R = 3
    C = 3
    for i in range(101):
        if r-1 < len(board) and c-1 < len(board[0]) and board[r-1][c-1] == k:
            answer = i
            break
        R = len(board)
        C = len(board[0])
        if R >= C:
            board = doR(board)
        else:
            board = doC(board)
        printB(board)
    print(answer)
