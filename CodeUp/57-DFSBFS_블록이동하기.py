# 오른쪽으로 이동 -> 벽이 있다 -> 아래로 회전
# 아래로 이동 벽이있다 오른쪽으로 회전
# 인자를 두개 받는다.!
board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [
    0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
n = len(board)

# [1번부품, 2번부품]
# 상하좌우, 1번고정2번위로,아래로, 2번고정 1번위롸,아래로
dx = [[-1, -1], [1, 1], [0, 0], [0, 0],  [0, -1], [0, 1], [-1, 0], [1, 0]]
dy = [[0, 0], [0, 0], [-1, -1], [1, 1],  [0, -1], [0, -1], [1, 0], [1, 0]]

# dfs에 2개좌표
# dfs가 좋을듯?
result = 1e9
count = 0


def dfs(x1, y1, x2, y2, count):
    global result
    if x1 < 0 or x2 < 0 or y1 < 0 or y2 >= n or y2 >= n or y2 >= n or y2 >= n or y2 >= n:
        return False
    else:
        # 방문처리

        if x1 == n-1 or x2 == n-1 or y1 == n-1 or y2 == n-1:
            result = min(count, result)
            return True
        else:

            if board[x1+dx[0][0]][y1+dy[0][0]] == 0 and board[x2+dx[0][1]][y2+dy[0][1]] == 0:
                board[x1+dx[0][0]][y1+dy[0][0]] = 2
                board[x2+dx[0][1]][y2+dy[0][1]] = 2
                dfs(x1+dx[0][0], y1+dy[0][0], x2 +
                    dx[0][1], y2+dy[0][1], count+1)
                board[x1+dx[0][0]][y1+dy[0][0]] = 0
                board[x2+dx[0][1]][y2+dy[0][1]] = 0
            if board[x1+dx[1][0]][y1+dy[1][0]] == 0 and board[x2+dx[1][1]][y2+dy[1][1]] == 0:
                board[x1+dx[1][0]][y1+dy[1][0]] = 2
                board[x2+dx[1][1]][y2+dy[1][1]] = 2
                dfs(x1+dx[1][0], y1+dy[1][0], x2 +
                    dx[1][1], y2+dy[1][1], count+1)
                board[x1+dx[1][0]][y1+dy[1][0]] = 0
                board[x2+dx[1][1]][y2+dy[1][1]] = 0
            if board[x1+dx[2][0]][y1+dy[2][0]] == 0 and board[x2+dx[2][1]][y2+dy[2][1]] == 0:
                board[x1+dx[2][0]][y1+dy[2][0]] = 2
                board[x2+dx[2][1]][y2+dy[2][1]] = 2
                dfs(x1+dx[2][0], y1+dy[2][0], x2 +
                    dx[2][1], y2+dy[2][1], count+1)
                board[x1+dx[2][0]][y1+dy[2][0]] = 0
                board[x2+dx[2][1]][y2+dy[2][1]] = 0
            if board[x1+dx[3][0]][y1+dy[3][0]] == 0 and board[x2+dx[3][1]][y2+dy[3][1]] == 0:
                board[x1+dx[3][0]][y1+dy[3][0]] = 2
                board[x2+dx[3][1]][y2+dy[3][1]] = 2
                dfs(x1+dx[3][0], y1+dy[3][0], x2 +
                    dx[3][1], y2+dy[3][1], count+1)
                board[x1+dx[3][0]][y1+dy[3][0]] = 0
                board[x2+dx[3][1]][y2+dy[3][1]] = 0

            # 1번고정 2번위로회전 -> 1번바로위와 2번위가 비어있어야함
            if board[x1-1][y1] == 0 and board[x2-1][y2] == 0:
                board[x1+dx[4][0]][y1+dy[4][0]] = 2
                board[x2+dx[4][1]][y2+dy[4][1]] = 2
                dfs(x1+dx[4][0], y1+dy[4][0], x2 +
                    dx[4][1], y2+dy[4][1], count+1)
                board[x1+dx[4][0]][y1+dy[4][0]] = 0
                board[x2+dx[4][1]][y2+dy[4][1]] = 0
            # 1번고정 2번아래회전
            if board[x1+1][y1] == 0 and board[x2+1][y2] == 0:
                board[x1+dx[5][0]][y1+dy[5][0]] = 2
                board[x2+dx[5][1]][y2+dy[5][1]] = 2
                dfs(x1+dx[5][0], y1+dy[5][0], x2 +
                    dx[5][1], y2+dy[5][1], count+1)
                board[x1+dx[5][0]][y1+dy[5][0]] = 0
                board[x2+dx[5][1]][y2+dy[5][1]] = 0
            # 2번고정 1번 위회전
            if board[x1+1][y1] == 0 and board[x2+1][y2] == 0:
                board[x1+dx[6][0]][y1+dy[6][0]] = 2
                board[x2+dx[6][1]][y2+dy[6][1]] = 2
                dfs(x1+dx[6][0], y1+dy[6][0], x2 +
                    dx[6][1], y2+dy[6][1], count+1)
                board[x1+dx[6][0]][y1+dy[6][0]] = 0
                board[x2+dx[6][1]][y2+dy[6][1]] = 0
            # 2번 고정 1번 아래회전
            if board[x1+1][y1] == 0 and board[x2+1][y2] == 0:
                board[x1+dx[7][0]][y1+dy[7][0]] = 2
                board[x2+dx[7][1]][y2+dy[7][1]] = 2
                dfs(x1+dx[7][0], y1+dy[7][0], x2 +
                    dx[7][1], y2+dy[7][1], count+1)
                board[x1+dx[7][0]][y1+dy[7][0]] = 0
                board[x2+dx[7][1]][y2+dy[7][1]] = 0


dfs(0, 0, 0, 1, count)
print(result)
print(board)
# DFS시류ㅐ!
