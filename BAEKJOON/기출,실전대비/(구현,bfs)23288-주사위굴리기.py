from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
#위, 오른쪽, 아래, 왼쪽


def moveDice(dice, d):
    if d == 0:
        temp = deque([dice[0][1], dice[1][1], dice[2][1], dice[3][1]])
        temp.append(temp.popleft())
        for i in range(4):
            dice[i][1] = temp[i]
    if d == 2:
        temp = deque([dice[0][1], dice[1][1], dice[2][1], dice[3][1]])
        temp.appendleft(temp.pop())
        for i in range(4):
            dice[i][1] = temp[i]
    if d == 1:
        temp = dice[1][0]
        dice[1][0] = dice[3][1]
        dice[1][1], temp = temp, dice[1][1]
        dice[1][2], temp = temp, dice[1][2]
        dice[3][1] = temp
    if d == 3:
        temp = dice[1][2]
        dice[1][2] = dice[3][1]
        dice[1][1], temp = temp, dice[1][1]
        dice[1][0], temp = temp, dice[1][0]
        dice[3][1] = temp


def changeDirection(d):
    if d == 0:
        return 2
    elif d == 1:
        return 3
    elif d == 2:
        return 0
    elif d == 3:
        return 1


def setDirection(A, B, d):
    if A > B:
        d += 1
        if d >= 4:
            d = 0
    elif A < B:
        d -= 1
        if d < 0:
            d = 3
    return d

# 이동할수있는 칸들의 개수


def grade(x, y):
    C = board[x][y]
    visited = [[0]*(m) for i in range(n)]
    cnt = 1
    q = deque()
    visited[x][y] = 1
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and board[nx][ny] == C:
                q.append((nx, ny))
                cnt += 1
                visited[nx][ny] = 1

    return cnt*C


def printd(dice):
    for i in dice:
        print(i)


if __name__ == '__main__':
    #아랫면 = 3,1
    n, m, k = map(int, input().split())
    dice = [[0, 2, 0], [4, 1, 3], [0, 5, 0], [0, 6, 0]]
    board = [list(map(int, input().split())) for i in range(n)]
    answer = 0
    d = 1
    now = [0, 0]
    for i in range(k):

        if 0 <= now[0]+dx[d] < n and 0 <= now[1]+dy[d] < m:
            now[0] += dx[d]
            now[1] += dy[d]
        else:
            d = changeDirection(d)
            now[0] += dx[d]
            now[1] += dy[d]
        moveDice(dice, d)
        answer += grade(now[0], now[1])

        d = setDirection(dice[3][1], board[now[0]][now[1]], d)

    print(answer)
