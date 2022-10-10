
import sys
input = sys.stdin.readline


# pos = 0 -> 가로
# pos = 1 -> 세로
# pos = 2 -> 대각선


def bt(x, y, pos):

    global answer
    if x == n-1 and y == n-1:
        answer += 1
    if pos == 0:  # 가로일때
        nx = x+0  # 가로
        ny = y+1
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 0:
                bt(nx, ny, 0)
        nx = x+1  # 대각선
        ny = y+1
        if 0 <= nx < n and 0 <= ny < n:
            if board[x+1][y+1] == 0 and board[x][y+1] == 0 and board[x+1][y] == 0:
                bt(nx, ny, 2)
    elif pos == 1:  # 세로일때
        nx = x+1  # 세로
        ny = y+0
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 0:
                bt(nx, ny, 1)
        nx = x+1  # 대각선
        ny = y+1
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 0 and board[x+1][y] == 0 and board[x][y+1] == 0:
                bt(nx, ny, 2)
    elif pos == 2:  # 대각선일때
        nx = x+1  # 세로
        ny = y+0
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 0:
                bt(nx, ny, 1)
        nx = x+0  # 가로
        ny = y+1
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 0:
                bt(nx, ny, 0)
        nx = x+1  # 대각선
        ny = y+1
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 0 and board[x+1][y] == 0 and board[x][y+1] == 0:
                bt(nx, ny, 2)


if __name__ == '__main__':
    answer = 0
    n = int(input())
    board = [list(map(int, input().split())) for i in range(n)]
    bt(0, 1, 0)
    print(answer)
