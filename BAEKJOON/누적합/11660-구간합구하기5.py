import sys
input = sys.stdin.readline
def getSum(sx, sy, ex, ey, board):

    return board[ex][ey]-board[sx-1][ey]-board[ex][sy-1]+board[sx-1][sy-1]


n, t = map(int, input().split())
board = []
board.append([0]*(n+1))
dp = [[0]*(n+1) for i in range(n+1)]
for i in range(1, n+1):
    board.append([0]+list(map(int, input().split())))

for i in range(1, n+1):
    board[1][i] = board[1][i-1]+board[1][i]
    board[i][1] = board[i-1][1]+board[i][1]


for i in range(2, n+1):
    for j in range(2, n+1):
        board[i][j] = board[i-1][j]+board[i][j-1]-board[i-1][j-1]+board[i][j]


result = []
for i in range(t):
    a, b, c, d = map(int, input().split())
    print(getSum(a, b, c, d, board))
