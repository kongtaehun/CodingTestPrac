# 행기준, 열기준 나눠서 생각해보자

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(str, list(input()))) for i in range(n)]
    dp_board = [[0]*(m) for i in range(n)]
    col = []
    row = []
    for i in range(n):
        flag = 0
        for j in range(m):
            if board[i][j] == 'X':
                flag = 0
                break
            else:
                flag = 1
        if flag == 1:
            col.append(i)
            for j in range(m):
                dp_board[i][j] += 1
    for j in range(m):
        flag = 0
        for i in range(n):
            if board[i][j] == 'X':
                flag = 0
                break
            else:
                flag = 1
        if flag == 1:
            row.append(j)
            for i in range(n):
                dp_board[i][j] += 1

    # print(dp_board)

    print(max(len(col), len(row)))
