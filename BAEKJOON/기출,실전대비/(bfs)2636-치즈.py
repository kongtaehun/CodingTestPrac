from collections import deque, Counter
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 1. bfs로 구명 찾기 -> 구멍은 0 배경은 -1로 만들기
#       0,0을 시작점으로 bfs한번만하면 구멍빼고 전부다 바꿀수있음


def findHole(board, visited, x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and board[nx][ny] == 0:
                    board[nx][ny] = -1
                    q.append((nx, ny))
                    visited[nx][ny] = 1


def findRmvPxl(board):
    result = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and (board[i+dx[0]][j+dy[0]] == -1 or board[i+dx[1]][j+dy[1]] == -1 or board[i+dx[2]][j+dy[2]] == -1 or board[i+dx[3]][j+dy[3]] == -1):
                board[i][j] = 0
                result += 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                cnt += 1
            if board[i][j] == -1:
                board[i][j] = 0
    # 현재 개수, 지운개수
    if cnt == 0:
        return False, result
    else:
        return True, result


# 2. 사방에 -1이 하나라도 있으면 제거
if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]
    answer = 0
    status = True
    while status:
        answer += 1
        visited = [[0]*(m) for i in range(n)]
        findHole(board, visited, 0, 0)
        status, result = findRmvPxl(board)
    print(answer)
    print(result)
