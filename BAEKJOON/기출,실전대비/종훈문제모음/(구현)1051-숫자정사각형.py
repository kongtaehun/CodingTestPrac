
def check(board, x, y, width):
    a = board[x][y]
    b = board[x+width][y]
    c = board[x][y+width]
    d = board[x+width][y+width]
    if a == b and b == c and c == d:
        return True
    else:
        return False


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, list(input()))) for i in range(n)]
    result = []
    for i in range(n):
        for j in range(m):
            for k in range(min(n-i, m-j)):
                if check(board, i, j, k):
                    result.append(k)
    print((max(result)+1)**2)
