
# n은 행


def dfs(x):
    global count
    if x == n:
        count += 1
        return

    else:
        # 열
        for i in range(n):
            # 퀸을 위치
            board[x] = i
            if check(x):
                dfs(x+1)


def check(x):
    for i in range(x):
        if board[i] == board[x] or abs(board[x]-board[i]) == abs(x-i):
            return False
    return True


if __name__ == '__main__':
    n = int(input())
    count = 0
    board = [0]*(n)
    dfs(0)
    print(count)
    # board = [[1, 1]]
    # x = 4
    # y = 3

    # print(check(x, y))
