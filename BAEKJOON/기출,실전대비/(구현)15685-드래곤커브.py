N = 100
# 드래곤커브 그리는 공간정의
# 드래곤커브그리는 메소드(dp?)


def setDragonCurve(x, y, direction, generation):
    global board
    moves = [[0, 0]]
    # 1세대 그리기
    if direction == 0:
        moves.append([1, 0])
    elif direction == 1:
        moves.append([0, -1])
    elif direction == 2:
        moves.append([-1, 0])
    else:
        moves.append([0, 1])

    # 90도 회전하기
    for i in range(generation):
        moves = rotate(moves)

    # 원점이동
    moves = moveCoord(x, y, moves)

    # board에 입력
    for x, y in moves:
        board[x][y] = 1


def rotate(moves):
    x, y = moves[-1]
    temp = []
    for i in range(len(moves)-1, -1, -1):
        temp.append([-(moves[i][1]-y), (moves[i][0]-x)])
        temp[-1][0] += x
        temp[-1][1] += y
    moves = moves+temp[1:]
    return moves

# 원점이동


def moveCoord(x, y, moves):
    for i in range(len(moves)):
        moves[i][0] += x
        moves[i][1] += y
    return moves

# 정사각형 개수 카운트


def countSquere(board):

    cnt = 0

    # 정사각형개수 카운트
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1 and board[i][j+1] == 1:
                if board[i+1][j] == 1 and board[i+1][j+1] == 1:
                    cnt += 1
    return cnt


if __name__ == '__main__':
    board = [[0]*(N+1) for i in range(N+1)]
    n = int(input())
    for _ in range(n):
        x, y, d, g = map(int, input().split())
        setDragonCurve(x, y, d, g)
    print(countSquere(board))
    # moves = [[0, 0], [1, 0]]
