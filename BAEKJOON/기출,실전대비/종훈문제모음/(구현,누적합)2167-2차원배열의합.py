def getArrSum(i, j, x, y, board):
    result = 0
    for a in range(i, x+1):
        for b in range(j, y+1):
            result += board[a][b]
    return result


def convertSumArr(board):
    temp = []
    temp.append([0]*(m+1))
    for i in range(n):
        temp.append([0]+board[i])

    for i in range(1, n+1):
        for j in range(1, m+1):
            temp[i][j] = temp[i-1][j-1]+temp[i][j-1] + \
                temp[i-1][j]+temp[i][j] - 2*temp[i-1][j-1]

    return temp


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]
    board = convertSumArr(board)
    for _ in range(int(input())):
        i, j, x, y = map(int, input().split())
        print(board[x][y] - board[x][j-1] - board[i-1][y]+board[i-1][j-1])
