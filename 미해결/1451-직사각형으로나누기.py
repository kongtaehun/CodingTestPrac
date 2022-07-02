
def getSumList(board):
    new_board = [[0]*(m+1) for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            new_board[i][j] = board[i-2][1] + \
                board[i-2][j-1]+board[i-1][j-1]-board[i-2][j-2]
    print(new_board)
    return new_board


n, m = map(int, input().split())
board = [list(map(int, list(input()))) for i in range(n)]
getSumList(board)


# #첫번쨰케이스
# for i in range(n-1):
#     for j in range(m-1):
#         첫번째 = [0,0] > [i,j]
#         두번째 = [i+1,0] > [n-1,j]
#         세번째 = [0,j+1] > [n-1,m-1]
