# 1. 10번이상해도 안될때 구현에서 실수가 있었다
# 2. visited 변수를 4차원으로 안하면 오류가 났었다.
# 3.  빨간공 파란공이 겹쳤을 때 (벽일경우 O일경우 복잡하였다.)
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def move(x, y, dx, dy):
    cnt = 0
    # 벽이거나 구멍까지
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


def bfs(board, q, visited):
    while q:
        rx, ry, bx, by, CNT = q.popleft()
        # print(rx, ry, bx, by)
        if CNT >= 10:  # 이부분의 차이때문에 틀림
            break

        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])

            if board[nbx][nby] != 'O':  # 실패조건
                if board[nrx][nry] == 'O':
                    return CNT+1
                if nrx == nbx and nry == nby:
                    # 이동거리가 큰것을 한칸뒤로
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                    # 겹쳤을 떄

                if visited[nrx][nry][nbx][nby] == 0:
                    visited[nrx][nry][nbx][nby] = 1
                    q.append((nrx, nry, nbx, nby, CNT+1))

    return -1


if __name__ == '__main__':
    n, m = map(int, input().split())

    board = [list(map(str, list(input()))) for i in range(n)]
    q = deque()
    visited = [[[[0] * m for _ in range(n)]
                for _ in range(m)] for _ in range(n)]
    r_roc = []
    b_roc = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                r_roc.append(i)
                r_roc.append(j)
            if board[i][j] == 'B':
                b_roc.append(i)
                b_roc.append(j)
    visited[r_roc[0]][r_roc[1]][b_roc[0]][b_roc[1]] = 1
    q.append((r_roc[0], r_roc[1], b_roc[0], b_roc[1], 0))
    print(bfs(board, q, visited))
    # print(checkCanGo(1, 5, board, 1, 4))
