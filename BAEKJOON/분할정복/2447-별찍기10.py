
def printArr(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                print(' ', end=' ')
            else:
                print('*', end=' ')
        print()


def dc(n):
    for startY in range(len(board)//n):
        for startX in range(len(board)//n):
            for i in range(n*startX+n//3, n*startX+2*(n//3)):
                for j in range(n*startY+n//3, n*startY+2*(n//3)):
                    board[i][j] = 0
    # if n!=3:
    #     dc(0,0,n//2)


n = int(input())
board = [['*']*n for i in range(n)]

while n != 1:
    dc(n)
    n = n//3
printArr(board)
