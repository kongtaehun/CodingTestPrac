from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def rotate(x, d, k):
    for i in range(n):
        if (i+1) % x == 0:
            if d == 0:
                for _ in range(k):
                    board[i].appendleft(board[i].pop())
            elif d == 1:
                for _ in range(k):
                    board[i].append(board[i].popleft())
# 4방향에 같은거있으면 지우기


def check(board):
    new_board = [[] for i in range(n)]
    checked = []
    flag = False
    for i in range(n):
        new_board[i] = [board[i][-1]]+list(board[i])+[board[i][0]]
    for i in range(n):
        for j in range(1, m+1):
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < n and new_board[nx][ny] != 0 and new_board[nx][ny] == new_board[i][j]:
                    flag = True
                    checked.append((i, j-1))
                    break

    for x, y in checked:
        board[x][y] = 0
    return flag


def setAvgBoard(board):
    sm = 0
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                cnt += 1
                sm += board[i][j]
    if cnt == 0:
        return
    avg = sm/cnt
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                if board[i][j] > avg:
                    board[i][j] -= 1
                elif board[i][j] < avg:
                    board[i][j] += 1


if __name__ == '__main__':
    # 원판수, 원판에적힌수 개수, 회전수
    n, m, t = map(int, input().split())
    board = []
    for i in range(n):
        board.append(deque(map(int, input().split())))

    for i in range(t):
        x, d, k = map(int, input().split())
        rotate(x, d, k)
        ch = check(board)

        if ch == False:
            setAvgBoard(board)

    print(sum(map(sum, board)))
