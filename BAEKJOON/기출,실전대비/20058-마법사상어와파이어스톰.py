# L에 따라 회전시키는 로직 구현
# 얼음인접개수 세서 얼음의 양 줄이기
# 덩어리 구하기
def rotate(l):
    temp_board = [[0]*n for i in range(n)]
    for i in range(n//l):
        x = i*l
        for j in range(n//l):
            y = j*l
            print(str(x)+'~'+str(x+l)+' ' + str(y)+'~'+str(y+l))
            for xx in range(x, x+l):
                for yy in range(y, y+l):
                    temp_board[yy][x+l-xx-1] = board[xx][yy]
    printB(temp_board)


def printB(board):
    for i in board:
        print(i)


if __name__ == '__main__':
    n, q = map(int, input().split())
    n = 2**n
    board = [list(map(int, input().split())) for i in range(n)]
    l_series = list(map(int, input().split()))
    l = 2
    printB(board)
    rotate(l)
