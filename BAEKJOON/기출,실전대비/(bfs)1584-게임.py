from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = 501


def bfs(x, y):
    q = deque()
    q.append((x, y))
    if board[x][y] == 2 and x != 0 and y != 0:
        return False
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 방문하지 않은지역 or 현재 생명력보다 더 적게 소모해서 갈 수 있을 경우 방문
                if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y]+board[nx][ny]:
                    if board[nx][ny] != 2:
                        # 위험지역일 경우 생명력을 소모하여 이동
                        if board[nx][ny] == 1:
                            visited[nx][ny] = visited[x][y] + 1
                            q.append((nx, ny))
                        # 안전지역일 경우 생명력을 소모하지 않고 이동
                        else:
                            visited[nx][ny] = visited[x][y]
                            q.append((nx, ny))

# 지역정보입력받기


def getZone():
    zone_cnt = int(input())
    zone = []
    for i in range(zone_cnt):
        x1, y1, x2, y2 = map(int, input().split())
        zone.append(
            (min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)))
    return zone


if __name__ == '__main__':
    # 위험,죽음지역 입력
    warn_zone = getZone()
    danger_zone = getZone()

    # board에 안전,위험,죽음지역 설정하기(우선순위 : Danger>Warn)
    board = [[0]*N for i in range(N)]
    visited = [[0]*N for i in range(N)]
    for i in warn_zone:
        for x in range(i[0], i[1]+1):
            for y in range(i[2], i[3]+1):
                board[x][y] = 1
    for i in danger_zone:
        for x in range(i[0], i[1]+1):
            for y in range(i[2], i[3]+1):
                board[x][y] = 2

    bfs(0, 0)
    print(visited[N-1][N-1]-1)
