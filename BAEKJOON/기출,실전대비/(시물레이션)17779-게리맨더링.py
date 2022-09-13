INF = int(1e9)


def check(board, temp):
    score = [0]*(6)
    for i in range(n):
        for j in range(n):
            score[temp[i][j]] += board[i][j]
    return max(score[1:]) - min(score[1:])


def divideLocal(x, y, d1, d2, board):

    temp = [[0]*(n) for i in range(n)]
    for i in range(n):
        for j in range(n):
            if 0 <= i < x+d1 and 0 <= j <= y:
                temp[i][j] = 1
            elif 0 <= i <= x+d2 and y < j < n:
                temp[i][j] = 2
            elif x+d1 <= i < n and 0 <= j < y-d1+d2:
                temp[i][j] = 3
            elif x+d2 < i < n and y-d1+d2 <= j < n:
                temp[i][j] = 4

    # 경계선
    temp[x][y] = 5
    for i in range(1, d2+1):
        temp[x+i][y+i] = 5
        temp[x+d1+i][y-d1+i] = 5
    for i in range(1, d1+1):
        temp[x+i][y-i] = 5
        temp[x+d2+i][y+d2-i] = 5
    for i in range(x+1, x+d1+d2):
        flag = 0
        for j in range(n):
            if temp[i][j] == 5:
                if flag == 1:
                    flag = 0
                    break
                if flag == 0:
                    flag = 1
                    continue
            if flag == 1:
                temp[i][j] = 5

    return check(board, temp)


def getPossibleRange(x, y):
    answer = INF
    for d1 in range(1, y+1):
        for d2 in range(1, n-y+1):
            if 0 <= y+d2 < n and 0 <= y-d1 < n and 0 <= x+(d1+d2) < n:
                answer = min(divideLocal(x, y, d1, d2, board), answer)
    return answer


if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input().split())) for i in range(n)]
    answer = INF
    for i in range(n-2):
        for j in range(1, n-1):
            answer = min(getPossibleRange(i, j), answer)
    print(answer)
