dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]


def cloudMoveRain(d, s, clouds):
    new_clouds = []
    for x, y in clouds:
        for _ in range(s):
            x = x+dx[d]
            if x >= n:
                x = 0
            elif x < 0:
                x = n-1
            y = y+dy[d]
            if y >= n:
                y = 0
            elif y < 0:
                y = n-1
        # 비내리기
        board[x][y] += 1
        new_clouds.append((x, y))
    return new_clouds


def copyRain(board, clouds):
    for x, y in clouds:
        if 0 <= x+1 < n and 0 <= y+1 < n and board[x+1][y+1] != 0:
            board[x][y] += 1
        if 0 <= x+1 < n and 0 <= y-1 < n and board[x+1][y-1] != 0:
            board[x][y] += 1
        if 0 <= x-1 < n and 0 <= y+1 < n and board[x-1][y+1] != 0:
            board[x][y] += 1
        if 0 <= x-1 < n and 0 <= y-1 < n and board[x-1][y-1] != 0:
            board[x][y] += 1


def createCloud(board, clouds):
    clouds = set(clouds)
    new_clouds = []
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and (i, j) not in clouds:
                new_clouds.append((i, j))
                board[i][j] -= 2
    return new_clouds


def countWater(board):
    answer = 0
    for i in range(n):
        for j in range(n):
            answer += board[i][j]
    return answer


def printB(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]
    clouds = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]
    for i in range(m):
        d, s = map(int, input().split())
        clouds = cloudMoveRain(d, s, clouds)
        copyRain(board, clouds)
        clouds = createCloud(board, clouds)
        # printB(board)
    print(countWater(board))
