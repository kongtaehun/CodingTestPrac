# 못잡은 예외 : 같은 거리에 있을 때 승객이 행더 작고 열더 작은 사람한테가야함
# 출발하는 곳에 손님이 있을 경우가 있음
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
# 그런 승객이 여러 명이면 그중 행 번호가 가장 작은 승객을, 그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객을 고른다.
# 한 승객을 목적지로 성공적으로 이동시키면, 그 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전된다
#  승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우는 실패한 것으로 간주하지 않는다.


def check(board):
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2:
                return False
    return True


def getDistPass(x, y, visited):
    result = []
    q = deque()
    visited[x][y] = 1
    q.append((x, y, 0))
    if board[x][y] >= 2:
        result.append((0, x, y))
    while q:
        x, y, cost = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] != 1:
                if board[nx][ny] >= 2:
                    result.append((cost+1, nx, ny))

                visited[nx][ny] = 1
                q.append((nx, ny, cost+1))

    if result:
        result.sort()

        return result[0][0], result[0][1], result[0][2]
    else:

        return -1, -1, -1


def getDistFromTo(x, y, visited):
    q = deque()
    if visited[x][y] == -1:
        return 0, x, y
    visited[x][y] = 1

    q.append((x, y, 0))
    while q:
        x, y, cost = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != 1 and board[nx][ny] != 1:
                if visited[nx][ny] == -1:
                    return cost+1, nx, ny
                visited[nx][ny] = 1
                q.append((nx, ny, cost+1))
    return -1, -1, -1


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]
    start_x, start_y = map(int, input().split())
    start_x -= 1
    start_y -= 1

    destination = [[] for i in range(m+2)]
    # 2부터 승객임
    for i in range(m):
        fx, fy, tx, ty = map(int, input().split())
        destination[i+2] = [tx-1, ty-1]
        board[fx-1][fy-1] = i+2

    false_flag = 0
    while True:
        # 가장가까운승객에게 가기
        visited = [[0]*(n) for i in range(n)]
        cost, x, y = getDistPass(start_x, start_y, visited)

        start_x, start_y = x, y
        k -= cost
        if k < 0 or cost == -1:
            false_flag = 1
            break
        # print(destination, board[x][y])
        tx, ty = destination[board[x][y]]
        board[x][y] = 0

        # 목적지까지 최단거리 계산
        visited = [[0]*(n) for i in range(n)]
        visited[tx][ty] = -1
        cost2, x, y = getDistFromTo(x, y, visited)
        start_x, start_y = x, y
        k -= cost2
        if k < 0 or cost2 == -1:

            false_flag = 1
            break
        k += 2*cost2

        if check(board):
            break

        # print(k, cost, cost2)
    if false_flag == 1:
        print(-1)
    else:
        print(k)
