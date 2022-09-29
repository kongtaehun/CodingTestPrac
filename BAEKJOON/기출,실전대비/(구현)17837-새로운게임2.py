dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def printB(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=' ')
        print()
    print("================")


def check(board):
    for i in range(n):
        for j in range(n):
            if len(board[i][j]) >= 4:
                return True
    return False


def move(num):

    x, y, d = piece[num]
    nx = x+dx[d]
    ny = y+dy[d]

    # 나의 위의 있는 것들가져오기
    temp = []
    item_idx = 0
    for i in range(len(piece_board[x][y])):
        if piece_board[x][y][i] == num:
            temp = piece_board[x][y][i:]
            item_idx = i
            piece_board[x][y] = piece_board[x][y][:i]
            break

    # 파란색일 경우
    if 0 > nx or 0 > ny or n <= nx or n <= ny or chess_board[nx][ny] == 2:

        # 방향전환
        if d == 0:
            d = 1
        elif d == 1:
            d = 0
        elif d == 2:
            d = 3
        elif d == 3:
            d = 2
        nx = x+dx[d]
        ny = y+dy[d]
        piece[num][2] = d
        if 0 <= nx < n and 0 <= ny < n and chess_board[nx][ny] != 2:
            pass
        else:
            piece_board[x][y] = piece_board[x][y]+temp
            return

    # 판이 흰색일 경우
    if chess_board[nx][ny] == 0:
        piece_board[nx][ny] = piece_board[nx][ny] + temp
    elif chess_board[nx][ny] == 1:
        temp.reverse()
        piece_board[nx][ny] = piece_board[nx][ny] + temp
    piece[num] = [nx, ny, d]
    for i in range(len(temp)):
        piece[temp[i]][0] = nx
        piece[temp[i]][1] = ny


if __name__ == '__main__':
    n, k = map(int, input().split())
    chess_board = [list(map(int, input().split())) for i in range(n)]
    piece_board = [[[] for _ in range(n)] for i in range(n)]
    piece = []
    for i in range(k):
        x, y, d = map(int, input().split())
        # 말올리기
        piece_board[x-1][y-1].append(i)
        piece.append([x-1, y-1, d-1])
    answer = -1
    for cnt in range(1001):

        for i in range(k):
            move(i)

            if check(piece_board):
                answer = cnt
                print(answer+1)
                exit(0)
    print(answer)
