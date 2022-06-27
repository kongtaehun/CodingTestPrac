# =========config=========
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

# ========func============
def dc(x, y, n):
    global result_mone, result_one, result_zero
    flag = board[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if board[i][j] != flag:
                dc(x, y, n//3)
                dc(x, y+n//3, n//3)
                dc(x, y+2*n//3, n//3)
                dc(x+n//3, y, n//3)
                dc(x+n//3, y+n//3, n//3)
                dc(x+n//3, y+2*n//3, n//3)
                dc(x+2*n//3, y, n//3)
                dc(x+2*n//3, y+n//3, n//3)
                dc(x+2*n//3, y+2*n//3, n//3)
                return
    if flag == 0:
        result_zero += 1
    elif flag == -1:
        result_mone += 1
    else:
        result_one += 1


# =========main===========
if __name__ == '__main__':
    n = int(input())
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))
    result_one = 0
    result_zero = 0
    result_mone = 0
    dc(0, 0, n)
    print(result_mone)
    print(result_zero)
    print(result_one)
