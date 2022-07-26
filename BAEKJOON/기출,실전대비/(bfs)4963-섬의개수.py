# 간단한 bfs/dfs 문제
# 비연결성 특성을 갖음 -> 모든노드에 대해서 bfs적용해야함
from collections import deque
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]


def bfs(board, visited, x, y, cnt):
    q = deque()
    q.append((x, y))
    visited[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if visited[nx][ny] == 0 and board[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = cnt


if __name__ == '__main__':

    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        board = [list(map(int, input().split())) for i in range(h)]
        visited = [[0]*w for i in range(h)]
        cnt = 1
        for i in range(h):
            for j in range(w):
                if board[i][j] == 1 and visited[i][j] == 0:
                    bfs(board, visited, i, j, cnt)
                    cnt += 1
        print(max(map(max, visited)))
