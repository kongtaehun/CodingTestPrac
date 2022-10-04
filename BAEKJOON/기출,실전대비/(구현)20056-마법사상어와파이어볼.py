# 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다.
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def printB(board):
    for i in board:
        print(i)


def getAnswer(board):
    answer = 0
    for i in range(n):
        for j in range(n):
            if len(board[i][j]) >= 1:
                for g, s, d in board[i][j]:
                    answer += g
    return answer


def move(board):
    temp_board = [[[] for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if len(board[i][j]) >= 1:
                while board[i][j]:
                    r = i
                    c = j
                    g, s, d = board[i][j].pop()
                    # 움직이는 거 반복문으로 구현
                    for _ in range(s):
                        r = r + dx[d]
                        c = c + dy[d]
                        if r >= n:
                            r = 0
                        elif r < 0:
                            r = n-1
                        if c >= n:
                            c = 0
                        elif c < 0:
                            c = n-1
                    temp_board[r][c].append((g, s, d))
    return temp_board

# #이동이 끝난뒤


def postproc(board):
    for i in range(n):
        for j in range(n):
            if len(board[i][j]) >= 2:
                sum_g = 0
                sum_s = 0
                cnt = len(board[i][j])
                odd_cnt = 0
                even_cnt = 0
                while board[i][j]:
                    g, s, d = board[i][j].pop()
                    if d % 2 == 0:
                        even_cnt += 1
                    else:
                        odd_cnt += 1
                    sum_g += g
                    sum_s += s
                # 정수,실수?
                s = sum_s//cnt
                g = sum_g//5
                if g == 0:
                    continue
                if (even_cnt == 0 and odd_cnt != 0) or (even_cnt != 0 and odd_cnt == 0):
                    board[i][j].append((g, s, 0))
                    board[i][j].append((g, s, 2))
                    board[i][j].append((g, s, 4))
                    board[i][j].append((g, s, 6))
                else:
                    board[i][j].append((g, s, 1))
                    board[i][j].append((g, s, 3))
                    board[i][j].append((g, s, 5))
                    board[i][j].append((g, s, 7))


if __name__ == '__main__':

    n, m, k = map(int, input().split())
    # 파이어볼 질량, 속도, 방향

    board = [[[] for i in range(n)] for i in range(n)]
    for i in range(m):
        r, c, g, s, d = map(int, input().split())
        board[r-1][c-1].append((g, s, d))

    for i in range(k):

        board = move(board)
        postproc(board)
    print(getAnswer(board))
